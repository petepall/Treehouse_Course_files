class Question():
    answer = None
    test = None


class Add(Question):
    def __init__(self, num1, num2):
        self.text = f"{num1} + {num2}"
        self.answer = num1 + num2


class Multiply(Question):
    def __init__(self, num1, num2):
        self.text = f"{num1} x {num2}"
        self.answer = num1 * num2
