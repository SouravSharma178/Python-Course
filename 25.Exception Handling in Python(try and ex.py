# Exception Handling in Python(try and except)

try:
    a = int(input("Enter the value for a "))
    b = int(input("Enter the value for b"))
    print(a / b)
except ZeroDivisionError:
    print('This is a division by zero error')  # this will get printed when the user enter value of b as 0
