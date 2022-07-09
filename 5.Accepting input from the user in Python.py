#Accepting input from the user in Python

# To take input from the user in python we would use the input function

#the code below would simply ask us to input the value
#this code would display the input without storing it in a variable

print(input("Please enter a value"))

#now in order to store it in a variable we would do the following task

#taking input from the user and storing it in a without defining the data type

a = (input("Please enter a value for a "))
print("the value of a is ",a)

#now in order to store it in a variable and define the data type we would do the following task

b = int(input("Please enter a integer value for b ")) #this will not take any input except integer
print("the value of a is ",b)

# we will do the same for string

c = str(input("Please enter a string value for c ")) #this will not take any input except string
print("the value of a is ",c)

# we will do the same for float

d = float(input("Please enter a float value for d ")) #this will not take any input except float
print("the value of a is ",d)

