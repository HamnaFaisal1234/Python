with open("1st.txt",'w')as file:
    file.write("My name is hamna")
    file.close()
    with open("1st.txt",'r')as file:
        data=file.readlines()
        print("I am the student of Codingal")
        for line in data:
            word=line.split()
            print(word)
            file.close()