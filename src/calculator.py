class Calculator:

    def __init__(self, sum1, sub1):
        self.sum1 = sum1
        self.sub1 = sub1
    
    def add(self, number1, number2, op):
        if op:
            return self.sum1.sum(number1, number2)
        return None
    
    def sub(self, number1, number2, op):
        if op:
            return self.sub1.sub(number1, number2)
        return None
