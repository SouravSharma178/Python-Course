#File handling(Reading data from a file)
file  = open("27.sample.txt",'r')  #we first created this text file called sample txt
content = file.read(10)            #10 here means we only want 10 bytes of data
print(content)
