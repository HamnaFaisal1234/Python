def longest(n):
    binary = bin(n)[2:]
    ones_groups = binary.split('0')
    max_length = max(len(group) for group in ones_groups)
    return max_length

number = int(input("Enter your number: "))
result = longest(number)
print("Longest consecutive 1's length:", result)
