#Passing/Using function as an argument of another function

def add(a,b):
    return a+b

def square(c):
    return c**2

result = square(add(2,3))  #calling the function
print(result)
