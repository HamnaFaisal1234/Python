
def numeral_simple(roman):
    values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    for i in range(len(roman) - 1):
        
        if values[roman[i]] < values[roman[i + 1]]:
            total -= values[roman[i]] 
        else:
            total += values[roman[i]]  
    
    
    total += values[roman[-1]]
    return total


user = input("Enter a Roman numeral: ")


print("The integer value is:", numeral_simple(user))
