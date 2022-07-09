#Best method to print user input in python

x = int(input("Please enter a value \n"))  #\n is the new line operator
print("This is the value for x"+" "+str(x)) #define the variable as string to print it
#this is show error if anything other than string is written,for example:

print("This is the value for x"+" "+int(x)) #defining it as an integer will show error
