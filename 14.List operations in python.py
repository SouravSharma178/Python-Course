#List operations in python
#we cannot multiply two lists in python

numbers = [1,1,1,1,1]
numbers[2] = 5       #inserting element 5 at index 2 in the list
print(numbers)

#joining two list together

numbers = [1,1,1,1,1]
newnumbers =[2,2,2,2,2]
print(numbers+newnumbers)
print(numbers*3)

#to check if a specific element is present in a list or not

fruits =["Apple", "Mango", "Peach"]

print("Apple" in fruits) #in is a built in python function to check if an element is present or not

print("oranges" in fruits)


