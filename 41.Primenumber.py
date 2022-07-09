#prime number in python
number = int(input("Enter the number \n"))
if(number==2):
    print("This number is prime")
def check():
    for i in range(2,number):
        if(number%i==0):
            print("this number is not prime")
            break
        else:
            print("This number is prime")
            break

check()