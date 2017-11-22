import functools

class OperationInvalidException(Exception):
    pass

class Operation(object):
    def __init__(self, *args):
        self.numbers = args

    def operate(self):
        raise NotImplementedError()


class AddOperation(Operation):
    # The only method present in this class
    def operate(self):
        return sum(self.numbers)


class SubtractOperation(Operation):
    def operate(self):
        return functools.reduce(lambda x, y: x - y, self.numbers)


class Calculator(object):
    def __init__(self, operations):
        self.operations = operations
    
    def calculate(self, *args):
        numbers, operation = args[:-1], args[-1]
        if operation in self.operations:  # if 'add' in operations
            o = self.operations[operation](*numbers)  # AddOperation(2, 2)
            return o.operate()
        else:
            raise OperationInvalidException("Invalid Operation")