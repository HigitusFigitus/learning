class Vehicle(object):
    def __init__(self, maker, model, year, base_price, miles):
        self.maker = maker
        self.model = model
        self.year = year
        self.base_price = base_price
        self.miles = miles
    
    def sale_price(self):
        return self.base_price * self.SALE_MULTIPLIER

    def purchase_price(self):
        return self.sale_price() - (self.PURCHASE_MULTIPLIER * self.miles)

class Car(Vehicle):
    def __init__(self, maker, model, year, base_price, miles):
        super(Car, self).__init__(maker, model, year, base_price, miles)
        self.SALE_MULTIPLIER = 1.2
        self.PURCHASE_MULTIPLIER = 0.004
        self.MONTHLY_INTEREST_RATE = 1.07
        self.LEASE_MULTIPLIER = 1.2


class Motorcycle(Vehicle):
    def __init__(self, maker, model, year, base_price, miles):
        super(Motorcycle, self).__init__(maker, model, year, base_price, miles)
        self.SALE_MULTIPLIER = 1.1
        self.PURCHASE_MULTIPLIER = 0.009
        self.MONTHLY_INTEREST_RATE = 1.03
        self.LEASE_MULTIPLIER = 1


class Truck(Vehicle):
    def __init__(self, maker, model, year, base_price, miles):
        super(Truck, self).__init__(maker, model, year, base_price, miles)
        self.SALE_MULTIPLIER = 1.6
        self.PURCHASE_MULTIPLIER = 0.02
        self.MONTHLY_INTEREST_RATE = 1.11
        self.LEASE_MULTIPLIER = 1.7
