from math import sqrt

number=int(input("Enter a number"))
print("\n")
if number>1:
    if number == 2:  
         print(number, "It is a prime number")
    else:
     for i in range(1,int(sqrt(number))+1):
        if (number % i)==0:
            print(number,"It is not a prime number")
            break
        else:
            print(number,"It is a prime number")
else:
        print(number, "It is not a prime number")
 


