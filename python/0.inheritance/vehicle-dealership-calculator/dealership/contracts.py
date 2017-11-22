class Contract(object):
    def __init__(self, vehicle, customer):
        self.vehicle = vehicle
        self.customer = customer

    def total_value():
        raise NotImplementedError
    
    def monthly_value():
        raise NotImplementedError
    
    def apply_discount(self, value):
        if self.customer.is_employee():
            value -= (value * 0.1)
        return value


class BuyContract(Contract):
    def __init__(self, vehicle, customer, monthly_payments):
        super(BuyContract, self).__init__(vehicle, customer)
        self.monthly_payments = monthly_payments

    def total_value(self):
        total_value = self.vehicle.sale_price() + \
            (self.vehicle.MONTHLY_INTEREST_RATE * \
            self.monthly_payments * self.vehicle.sale_price() / 100)
        return self.apply_discount(total_value)
    
    def monthly_value(self):
        return self.total_value() / self.monthly_payments


class LeaseContract(Contract):
    def __init__(self, vehicle, customer, length_in_months):
        super(LeaseContract, self).__init__(vehicle, customer)
        self.length_in_months = length_in_months

    def total_value(self):
        total_value = self.vehicle.sale_price() + \
        (self.vehicle.sale_price() * self.vehicle.LEASE_MULTIPLIER \
        / self.length_in_months)
        return self.apply_discount(total_value)
    
    def monthly_value(self):
        return self.total_value() / self.length_in_months
