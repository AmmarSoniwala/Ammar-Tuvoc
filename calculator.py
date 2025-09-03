class Calculator:
    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Error! Division by Zero."
        return a / b
    
calc = Calculator()
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

ch = input("Enter operation (+, -, *, /): ")

match ch:
    case '+':
        print(f"{num1} + {num2} = {calc.add(num1,num2)}")
    case '-':
        print(f"{num1} - {num2} = {calc.subtract(num1,num2)}")
    case '*':
        print(f"{num1} * {num2} = {calc.multiply(num1,num2)}")
    case '/':
        print(f"{num1} / {num2} = {calc.divide(num1,num2)}")
    case _:
        print("Enter a valid operation.")