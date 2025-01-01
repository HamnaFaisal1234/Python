def setornot(n,number):
    first = 1
    if (n&first)==1 or (n&first) ==0:
        if number&(1<<(n-1)):
            print("Set")
        else:
            print("Not set")
number = int(input("Enter a number:"))
n = int(input("Enter a bit position"))
setornot(n,number)           