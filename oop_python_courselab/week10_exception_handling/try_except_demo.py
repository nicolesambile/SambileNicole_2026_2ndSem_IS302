try:
    number_nbs = int(input("Enter a number: "))
    result_nbs = 100 / number_nbs
    print("Result:", result_nbs)
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Invalid input")

#Nicole B. Sambile