# List slicing in python
# List slicing refers to cutting out our list into smaller parts

numbers = [1, 2, 3, 4, 5]
print(numbers[0:6])  # the starting is inclusive but the end is exclusive that is why 6 has been written instead of 5

print(numbers[0:])  # if no end has been specified then the list will go unto the end

print(numbers[:])  # if no start and end has been specified then the list will go unto the end as well

print(numbers[0:6:1])  # intervals can also be defined for the list to print

print(numbers[0:6:2])  # this will skip the interval-1 values so writing 2 will only skip one value

print(numbers[0:6:3])  # this will skip two values

