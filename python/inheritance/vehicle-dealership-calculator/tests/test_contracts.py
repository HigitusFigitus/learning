from pytest import approx

from dealership.contracts import BuyContract, LeaseContract
from dealership.customers import Customer, Employee
from dealership.vehicles import Car, Truck, Motorcycle


car = Car(
    maker='Ford', model='Mustang', year=2005, base_price=18000, miles=31000)

truck = Truck(
    maker='Chevrolet', model='Silverado', year=2014,
    base_price=29000, miles=3000)

bike = Motorcycle(
    maker='Ducati', model='Monster', year=2016, base_price=18000, miles=700)

customer = Customer('John', 'Doe', 'john@example.com')
employee = Employee('Jane', 'Doe', 'jane@example.com')


def test_buy_contract_total_value_with_customer():
    car_contract = BuyContract(
        vehicle=car, customer=customer, monthly_payments=6)

    assert car_contract.total_value() == approx(22986.72, rel=1e-5)
    assert car_contract.monthly_value() == approx(3831.12, rel=1e-5)

    truck_contract = BuyContract(
        vehicle=truck, customer=customer, monthly_payments=12)

    assert truck_contract.total_value() == approx(52580.47, rel=1e-5)
    assert truck_contract.monthly_value() == approx(4381.70, rel=1e-5)

    bike_contract = BuyContract(
        vehicle=bike, customer=customer, monthly_payments=36)

    assert bike_contract.total_value() == approx(27141.84, rel=1e-5)
    assert bike_contract.monthly_value() == approx(753.94, rel=1e-5)


def test_buy_contract_total_value_with_employee():
    car_contract = BuyContract(
        vehicle=car, customer=employee, monthly_payments=6)

    car_contract.total_value() == approx(20688.04, rel=1e-5)
    car_contract.monthly_value() == approx(3448, rel=1e-5)

    truck_contract = BuyContract(
        vehicle=truck, customer=employee, monthly_payments=12)

    assert truck_contract.total_value() == approx(47322.43, rel=1e-5)
    assert truck_contract.monthly_value() == approx(3943.53, rel=1e-5)

    bike_contract = BuyContract(
        vehicle=bike, customer=employee, monthly_payments=36)

    assert bike_contract.total_value() == approx(24427.65, rel=1e-5)
    assert bike_contract.monthly_value() == approx(678.54, rel=1e-5)


def test_lease_contract_total_value_with_customer():
    car_contract = LeaseContract(
        vehicle=car, customer=customer, length_in_months=12)

    assert car_contract.total_value() == approx(23760.0, rel=1e-4)
    assert car_contract.monthly_value() == approx(1980.0, rel=1e-4)

    truck_contract = LeaseContract(
        vehicle=truck, customer=customer, length_in_months=24)

    assert truck_contract.total_value() == approx(49686.66, rel=1e-4)
    assert truck_contract.monthly_value() == approx(2070.27, rel=1e-4)

    bike_contract = LeaseContract(
        vehicle=bike, customer=customer, length_in_months=36)

    assert bike_contract.total_value() == approx(20350, rel=1e-4)
    assert bike_contract.monthly_value() == approx(565.27, rel=1e-4)
