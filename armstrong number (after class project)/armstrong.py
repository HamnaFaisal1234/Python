# Armstrong Number Checker
# This program checks if a given number is an Armstrong number.
# An Armstrong number is equal to the sum of its own digits raised to the power of the number of digits.
def is_armstrong(num):
    total = sum(int(digit) ** len(str(num)) for digit in str(num))
    return total == num
user_input = int(input("Enter a number: "))
if is_armstrong(user_input):
    print(f"{user_input} is an Armstrong number.")
else:
    print(f"{user_input} is not an Armstrong number.")
