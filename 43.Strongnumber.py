#armstrong number(sum of cubes)
number = int(input("enter the number \n"))
numberstore = number
count = len(str(number))
print(count)
cube = 0
for i in range(1,count+1):
    temp = number%10
    cube = cube + pow(temp,count)
    number = number/10
print(cube)
if(cube==numberstore):
    print("this number is an armstrong number")
else:
     print("this number is not an armstrong number")