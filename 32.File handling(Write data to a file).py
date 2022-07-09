##File handling(Write data to a file)
file = open("31.writefile.txt",'w')  #w here represents write
file.write("This is the text written to the file") #for this we will use the write function
file.close()


#we can directly read the content of the file from here
file = open("31.writefile.txt",'r')

content = file.read()
print(content)
file.close()

#once a file is closed we can only read it
#if we try to write a file again the file will have this new text and the old text will be deleted
#for this reason we will use the append mode