class Calculator:
    def __init__(self, expression):
        self.expression = expression

    def evaluate(self):
        return eval(self.expression)


expression = input("Enter a mathematical expression: ")
calculator = Calculator(expression)
result = calculator.evaluate()
print(f"The result of '{expression}' is: {result}")
