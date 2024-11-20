file1 = open("3rd.txt", 'r')
file2 = open("4rth.txt", 'w')
for line in file1.readlines():
    if not (line.startswith("codingal")):
        print(line)
        file2.write(line)
file1.close()
file2.close()