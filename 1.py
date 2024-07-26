#Claro, aquí tienes un ejemplo de código Python para crear una calculadora sencilla:


def add(num1, num2):
    """Suma dos números juntos"""
    return num1 + num2

def subtract(num1, num2):
    """Resta el segundo número del primer número"""
    return num1 - num2

def multiply(num1, num2):
    """Multiplica dos números juntos"""
    return num1 * num2

def divide(num1, num2):
    """Divide el primer número por el segundo número"""
    return num1 / num2

def power(num, exponent):
    """Eleva el primer número a la potencia del segundo número"""
    return num ** exponent

def calculate(operation, num1, num2):
    """Realiza una operación matemática con dos números"""
    if operation == "+":
        return add(num1, num2)
    elif operation == "-":
        return subtract(num1, num2)
    elif operation == "*":
        return multiply(num1, num2)
    elif operation == "/":
        return divide(num1, num2)
    elif operation == "^":
        return power(num1, num2)
    else:
        raise ValueError("Operación inválida")

while True:
    try:
        num1 = float(input("Introduce el primer número: "))
        operation = input("Ingrese a la operación (+, -, *, /, ^): ")
        num2 = float(input("Ingrese el segundo número: "))
        result = calculate(operation, num1, num2)
        print(f"{num1} {operation} {num2} = {result}")
    except ValueError as e:
        print(e)
