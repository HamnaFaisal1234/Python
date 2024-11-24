with open ("New1.txt")as fp:
    data1=fp.read()
with open ("soft.txt")as fp:
    data2=fp.read()
data1 +="\n"
data1 +=data2
print("Merging two file...")
with open ("Happy.txt","w") as fp:
    fp.write (data1)
