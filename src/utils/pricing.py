import random


def discount(subtotal):

    if random.random() < 0.15:

        return round(subtotal * random.uniform(0.05,0.20),2)

    return 0


def tax(amount):

    return round(amount*0.05,2)