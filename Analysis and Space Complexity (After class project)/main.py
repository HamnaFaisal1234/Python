def myfunction1(n):
    if (n <= 0): 
        return
    for i in range(0, int(n) + 1):  
        print("Hi👋🏻! Welcome")
    myfunction1(int(n / 2))  
    myfunction1(int(n / 3))  


myfunction1(6)  
def myfunction2(n):
    if (n <= 1):  
        return
    print("I am Hamna") 
    myfunction2(n - 1)  


myfunction2(5)  
