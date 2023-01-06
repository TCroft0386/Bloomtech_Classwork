from acme import Product
from acme import random

ADJECTIVES = ["Awesome", "Shiny", "Impressive", "Portable", "Improved"]
NOUNS = ["Anvil", "Catapult", "Disguise", "Mousetrap", "???"]


def generate_products(num=30):
    '''Generates a list of Products a certain amount of times. Default = 30'''
    product_list = []
    for _ in range(num):
        product_list.append(Product(
            name=random.choice(ADJECTIVES)+' '+random.choice(NOUNS),
            price=random.randint(5, 100),
            weight=random.randint(5, 100),
            flammability=random.uniform(0, 2.5)))
    return product_list


def average(lst):
    '''average of list'''
    return sum(lst)/len(lst)


def inventory_report(product_list):
    '''takes each value out of generate_Products and finds the average'''
    unique = []
    price = []
    weight = []
    flammability = []
    for i in product_list:
        unique.append(i.name)
        price.append(i.price)
        weight.append(i.weight)
        flammability.append(i.flammability)
    return (len(set(unique)), average(price), average(weight),
            average(flammability))
