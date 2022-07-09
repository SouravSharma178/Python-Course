##File handling(Write data to a file)
file = open("31.writefile.txt",'w')  #w here represents write
file.write("This is the text written to the file") #for this we will use the write function
file.close()


#we can directly read the content of the file from here
file = open("31.writefile.txt",'r')

content = file.read()
print(content)
file.close()

file = open("31.writefile.txt",'a')  #a here represents append
file.write("This is the new text \n")
file.close()

#check the text file for changes