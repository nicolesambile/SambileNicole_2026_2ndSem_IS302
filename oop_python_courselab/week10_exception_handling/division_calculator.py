try:
    num1_nbs = float(input("Enter first number: "))
    num2_nbs = float(input("Enter second number: "))
    result = num1_nbs / num2_nbs
    print("Result:", result)
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Invalid numeric input")

#Nicole B. Sambile