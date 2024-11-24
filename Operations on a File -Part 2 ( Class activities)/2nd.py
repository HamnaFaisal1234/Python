newfile=open("New1.txt", 'x')
newfile.close()
import os
print("Checking if 1st.file exits or not....")
if os.path.exists ("2nd.txt"):
    os.remove("2nd.txt")
else:
    print("The file does not exists")
myfile=open('Soft.txt','w')
myfile.write("hey i am Hamna")
myfile.close()
os.remove('New.txt')
os.rmdir('Folder')
