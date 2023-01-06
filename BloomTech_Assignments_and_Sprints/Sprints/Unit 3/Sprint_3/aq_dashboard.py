from flask import Flask
from openaq import OpenAQ
from flask_sqlalchemy import SQLAlchemy

"""OpenAQ Air Quality Dashboard with Flask."""
FLASK_ENV = 'development'

app = Flask(__name__)
api = OpenAQ()
DB = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
DB.init_app(app)


@app.route('/')
def root():
    """Base view."""
    record = Record.query.filter(Record.value >= 18).all()
    return str(record)


def get_results():
    body, status = api.measurements(city='Los Angeles', parameter='pm25')
    utc = []
    for i in status['results']:
        utc.append((i['date']['utc'], i['value']))
    return utc


class Record(DB.Model):
    # id (integer, primary key)
    id = DB.Column(DB.Integer, primary_key=True, nullable=False)
    # datetime (string)
    datetime = DB.Column(DB.String)
    # value (float, cannot be null)
    value = DB.Column(DB.Float, nullable=False)
    # YOUR CODE HERE

    def __repr__(self):
        return f'''ID: {self.id},
                Date: {self.datetime},
                Value: {self.value}'''.format(self.id,
                                              self.datetime,
                                              self.value)


@app.route('/refresh')
def refresh():
    """Pull fresh data from Open AQ and replace existing data."""

    DB.drop_all()
    DB.create_all()
    # TODO Get data from OpenAQ, make Record objects with it, and add to db

    for data in get_results():
        db_data = Record(datetime=data[0], value=data[1])
        DB.session.add(db_data)
    DB.session.commit()
    return 'Data refreshed!'
