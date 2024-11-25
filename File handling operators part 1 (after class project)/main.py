
#read the beginning 10 letters of the line
file = open ("hi.txt","r")
print("Read the beginning 10 letters\n",file.read(10),"\n\n\n")
file.close()

#read the first line of the content 
file = open ("hi.txt","r")
print("Read the first line of the content\n",file.readline(),"\n\n\n")
file.close()

#read the first five lines of the content 
file = open ("hi.txt","r")
print("Read the first five lines of the content")
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline(),"\n\n\n")
file.close()

#read all the lines of the content 
file = open ("hi.txt","r")
print("Read all the lines of the content\n",file.readlines(),"\n\n\n")
file.close()