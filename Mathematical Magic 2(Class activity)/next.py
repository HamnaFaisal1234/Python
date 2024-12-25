def sieve(num):
    prime = [True for i in range(num + 1)]  
    p = 2
    while (p * p <= num):  
        if prime[p]:  
            for i in range(p * p, num + 1, p):  
                prime[i] = False
        p += 1  

    print("Following are the prime numbers smaller than or equal to", num)
    for p in range(2, num + 1):
        if prime[p]:  
            print(p, end=" ")


num = int(input("Enter a number: "))
sieve(num)




