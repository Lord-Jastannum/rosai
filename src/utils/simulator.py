import random
from datetime import datetime, timedelta


class RestaurantSimulator:

    def __init__(self):

        self.breakfast = (8, 11)
        self.lunch = (12, 15)
        self.dinner = (18, 22)

    def random_time(self):

        r = random.random()

        if r < 0.20:
            hour = random.randint(8, 11)

        elif r < 0.60:
            hour = random.randint(12, 15)

        else:
            hour = random.randint(18, 22)

        minute = random.randint(0, 59)

        return hour, minute

    def orders_today(self, weekend):

        if weekend:
            return random.randint(60, 100)

        return random.randint(30, 70)

    def order_type(self):

        return random.choices(

            ["Dine In", "Takeaway", "Delivery"],

            weights=[50, 20, 30]

        )[0]

    def payment_method(self):

        return random.choices(

            ["Card", "Cash", "UPI"],

            weights=[55, 15, 30]

        )[0]