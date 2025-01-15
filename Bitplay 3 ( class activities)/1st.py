def divide(dividend, divisor):
    
    sign = (-1 if ((dividend < 0) ^ (divisor < 0)) else 1)
    
    dividend = abs(dividend)
    divisor = abs(divisor)
    
    quotientNumber = 0
    tempNumber = 0
    
    for i in range(31, -1, -1):
        if (tempNumber + (divisor << i) <= dividend):
            tempNumber += divisor << i
            quotientNumber += 1 << i
    
    quotientNumber *= sign
    
    INT_MAX = 2**31 - 1
    INT_MIN = -2**31
    if quotientNumber < INT_MIN:
        return INT_MIN
    if quotientNumber > INT_MAX:
        return INT_MAX
    
    return quotientNumber

print(divide(10, 3))  
print(divide(7, -3)) 




