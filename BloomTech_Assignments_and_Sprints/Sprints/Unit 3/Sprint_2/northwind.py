import sqlite3
# Import sqlite3

conn = sqlite3.connect('demo_data.sqlite3')
# Set up a connection to database.

cursor = conn.cursor()
# Set up a cursor


def execute_query(conn, query):
    "Executing a query"
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()


expensive_items = '''SELECT * FROM Product GROUP BY UnitPrice
ORDER BY UnitPrice DESC LIMIT 10'''

avg_hire_age = '''SELECT AVG(employee.HireDate - Employee.BirthDate)
                FROM employee'''


ten_most_expensive = '''SELECT ProductName, UnitPrice,CompanyName FROM Product
JOIN Supplier WHERE Supplier.id=Product.SupplierId ORDER BY UnitPrice
DESC LIMIT 10'''

largest_category = '''SELECT MAX(Category.CategoryName),
COUNT( DISTINCT Product.ProductName) AS cat_count FROM Product
JOIN Category ON Product.CategoryId = Category.Id
GROUP BY Category.CategoryName ORDER BY cat_count DESC LIMIT 1'''
