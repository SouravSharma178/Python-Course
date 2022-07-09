#list operations in python
fruits =["Apple", "Mango", "Peach", "Orange"]

fruits.append("Banana")   #append - to add new item to the list

print(fruits)


print(len(fruits))        #length provides length of the list
fruits.insert(1,"Banana") #insert adds values at the index defined
print(fruits)

print(fruits.index("Orange"))  #index shows at which place the element exists
