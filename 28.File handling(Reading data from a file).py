#File handling(Reading data from a file)
file  = open("27.sample.txt",'r')  #we first created this text file called sample txt
content = file.read()              #when we read data from a file we need a variable to store it
print(content)

