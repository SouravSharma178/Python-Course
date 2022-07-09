#File handling(Reading data from a file)
file  = open("27.sample.txt",'r')  #we first created this text file called sample txt,the r here means we only want to read the file not write it
content = file.readline()          #The readline function prints just one line of the file
print(content)
