number = input("enter a number to check weather it is armstrong or not")
result =  int(number[0])**3 + int(number[1])**3 + int(number[2])**3

if (result==int(number)):
    print(number," is an armstrong number")
else:
    print(number,"is not an armstrong number")