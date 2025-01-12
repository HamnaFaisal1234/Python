def power(n):
    
    return n > 0 and (n & (n - 1)) == 0 and bin(n).count('0') % 3 == 1

n = int(input("Enter a number: "))
print(n,"is a power of 8: ",power(n))

