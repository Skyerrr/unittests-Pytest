from faker import Faker

faker = Faker()

class SubOperationSpy:

    def __init__(self):
        self.sub_attributes = {}

    def sub(self, number1, number2):
        self.sub_attributes['number1'] = number1
        self.sub_attributes['number2'] = number2

        return faker.random_number()
