import random


class Product:
    '''Products class'''

    def __init__(self, name, identifier=random.randint(999999, 10000000),
                 price=10, weight=20, flammability=0.5):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = identifier

    def stealability(self):
        '''price / weight = stealability'''
        if self.price / self.weight < 0.5:
            return 'Not so stealable'
        if 0.5 <= self.price / self.weight < 1.0:
            return 'kinda stealable'
        else:
            return 'Very stealable'

    def explode(self):
        '''flammability * weight = explode?'''
        value = self.flammability * self.weight
        if value < 10:
            return '...fizzle'
        if 10 >= value < 50:
            return '...boom!'
        else:
            return '...BABOOM!!'


class BoxingGlove(Product):
    '''Boxing Glove class'''

    def __init__(self, name, identifier=random.randint(999999, 10000000),
                 price=10, flammability=0.5, weight=10):
        self.weight = weight
        super().__init__(name, identifier, price, weight, flammability)

    def explode(self):
        return'...its a glove.'

    def punch(self):
        '''punch'''
        if self.weight < 5:
            return 'That tickles'
        if 5 <= self.weight < 15:
            return 'Hey that hurt!'
        else:
            return 'OUCH!'
