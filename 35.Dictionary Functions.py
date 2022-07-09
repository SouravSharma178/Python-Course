# Dictionary Functions

numbers = {1: "one", 2: "two", 3: "three"}
print(numbers[1])  # this would show the key at this value
print(numbers.get(2))  # the get function would do the same

print(numbers.get(5))  # get will display a none value if there is no key available

print(numbers.get(5,
                  "Key not found"))  # if we want to replace none which is the default we can write a new statement
# when using a comma

print(1 in numbers)  # check if 1 is present in the dictionary

print(5 in numbers)
