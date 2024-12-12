import math
def prints(n):
    if (n<=0):
        return
    print(round (n,2),"Hamna")
    prints(n**3)
    
prints(3)