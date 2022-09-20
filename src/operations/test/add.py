from faker import Faker

faker = Faker()

class AddOperationSpy:

    def __init__(self):
        self.sum_attributes = {}

    def sum(self, number1, number2):
        self.sum_attributes['number1'] = number1
        self.sum_attributes['number2'] = number2

        return faker.random_number()
