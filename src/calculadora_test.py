from faker import Faker
from .operations.test.add import AddOperationSpy
from .operations.test.sub import SubOperationSpy
from .calculator import Calculator

fake = Faker()

def test_add():
    addOperation = AddOperationSpy()
    subOperation = SubOperationSpy()
    calculator = Calculator(addOperation, subOperation)

    number1 = fake.random_number()
    number2 = fake.random_number()

    result = calculator.add(number1, number2, True)

    # Testing input
    assert addOperation.sum_attributes['number1'] == number1
    assert addOperation.sum_attributes['number2'] == number2

    # Testing output
    assert result is not None


def test_sub():
    addOperation = AddOperationSpy()
    subOperation = SubOperationSpy()
    calculator = Calculator(addOperation, subOperation)

    number1 = fake.random_number()
    number2 = fake.random_number()

    result = calculator.sub(number1, number2, True)

    # Testing input
    assert subOperation.sub_attributes['number1'] == number1
    assert subOperation.sub_attributes['number2'] == number2

    # Testing output
    assert result is not None
