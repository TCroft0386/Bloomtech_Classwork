from acme import Product
from acme_report import generate_products


def test_default_product_price():
    '''Test default Product price being 10.'''
    prod = Product('Test Product')
    assert prod.price == 10


def stealability_test():
    '''makes sure function works inside acme.py'''
    prod = Product('Test Product', weight=40)
    assert prod.stealability == 'Very Stealable'


def explode_test():
    '''makes sure function works inside acme.py'''
    prod = Product(weight=24, flammability=2)
    assert prod.explode == '...boom!'


def generator_test():
    '''makes sure function works inside acme.py'''
    assert len(generate_products) == 30
