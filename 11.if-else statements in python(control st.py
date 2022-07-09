#if-else statements in python(control structures)
age = int(input('enter your age \n'))
if age >= 18:
    print('You are an adult') #as long as anything is written with the same
    print('You can drive')    #indentation under this print statement it will be considered a part of this
else:                         #since else is not directly under the print,it is separate from if
    print( 'You are not an adult')


'''
age = int(input('enter your age \n'))
if age >= 18:
print('You are an adult')

#this program will produce an error as print will no longer be considered a part of if

else:
print( 'You are not an adult')
'''


