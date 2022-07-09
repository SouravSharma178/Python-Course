#List Comprehensions,allows which defines rules for a list

#the first part elements**2 represents the mathematical operations and

# the second part represents the values upto which we want to calulate

list = [elements**2 for elements in range(1,6)]
print("The list which contains square of numbers from"+str(list))

#Further we can also add conditions to this list

#this list will only contain square of even numbers,only even squares
list2 = [values**2 for values in range(1,6) if values**2 % 2 == 0 ]
print(list2)

