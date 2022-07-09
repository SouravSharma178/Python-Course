#Exception Handling in Python(Finally Block)

try:
    a = int(input("Enter the value for a "))
    b = int(input("Enter the value for b"))
    print(a/b)
except ZeroDivisionError:
    print('This is a division by zero error') #this will get printed when the user enter value of b as 0

finally:
    print("This is going to execute no matter what") #This block is going to execute regardless
