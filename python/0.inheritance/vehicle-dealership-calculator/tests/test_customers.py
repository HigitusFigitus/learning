from dealership.customers import Customer, Employee


def test_customer_is_not_employee():
    c = Customer('John', 'Doe', 'john@example.com')
    assert c.first_name == 'John'
    assert c.last_name == 'Doe'
    assert c.email == 'john@example.com'

    assert c.is_employee() is False


def test_customer_is_employee():
    e = Employee('Jane', 'Doe', 'jane@example.com')
    assert e.first_name == 'Jane'
    assert e.last_name == 'Doe'
    assert e.email == 'jane@example.com'

    assert e.is_employee() is True
