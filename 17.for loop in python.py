#for loop in python

for x in range(1,11):  #the element 1 is inclusive but element 11 is exclusive
    print(x)

fruits = ["Apple","Mango","Peach","Banana"]
for x in fruits:       # x is same as i here just like in c/c++
    print(x)

# program to print even number from 1 to 20:

for i in range(0,21):
    if i%2 == 0:
        print(i)


#alternative way to do this is
for i in range(0,21,2):
        print(i)
