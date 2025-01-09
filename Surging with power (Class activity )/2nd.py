def power4(number1):
    count = 0
    if (number1 & (~(number1 & (number1-1)))):
       while (number1 > 1):
             number1 >>=1
             count+=1
    if (count % 2 ==0):
        return True
    else:
        return False

number1 = int(input("Enter a number:"))
if power4(number1):
    print(number1, "\n The number is a power of 4")
else:
    print(number1,"\n The number is not a power of 4")