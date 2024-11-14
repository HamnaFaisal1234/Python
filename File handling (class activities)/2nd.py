f1=open('first.txt','r')
f2=open('myfile.txt','r')

f1.read()
f2.read()

f1.close()
f2.close()

f1=open('first.txt','a+')
f2=open('myfile.txt','r')

f1.write(f2.read())
f1.seek(0)
f2.seek(0)

print('content from first file before append _\n',f1.read())
print('content from second file after append _\n',f2.read())

f1.close()
f2.close()