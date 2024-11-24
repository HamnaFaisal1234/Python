with open ("My-File.txt" , "w") as f :
    f.write("My name is Hamna\nMy father name is Faisal\nI live in Pakistan\nI read in grade 11 \nI like Mango \nMy favorite color is Pink ")
    
with open ("My-File.txt" , "r") as f :
    content = f.read()
    words = content.split()
    print(words)
import os 
print("Checking if My-new-File.txt exist or not...")
if os.path.exists("My-new-File.txt"):
     print("File exist" )
else: 
     print("File does not exist")
outputfile = open("My-new-File.txt" , "w")
inputfile = open("My-File.txt" , "r")
Lines =set()
for line in inputfile:
    if line not in Lines:
             outputfile.write(line)
             Lines.add(line)
inputfile.close()
outputfile.close()
os.remove("Want to delete file.txt")
