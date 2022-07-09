#Strong number
number = int(input("enter the number \n"))
numberstore = number
count = len(str(number))
print(count)
temp2 = 0
for i in range(0,count):
    product = 1
    temp = number%10
    for i in range(1,temp+1):
            product = (product*i)
    temp2 = temp2 + product
    print(temp2)
    number = number/10
if(temp2==numberstore):
    print("This number is a strong number")
else:
    print("This number is not a strong number")