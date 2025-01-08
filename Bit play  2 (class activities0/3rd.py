def two_odd(arr):
    xor_all = 0
    for element in arr:
        xor_all ^= element

    rightmost_set_bit = xor_all & -xor_all

    num1, num2 = 0, 0
    for element in arr:
        if element & rightmost_set_bit:
            num1 ^= element  
        else:
            num2 ^= element  

    return num1, num2

arr = []

n = int(input("Enter array size: "))
print("Enter array elements:")

while n:
    num = int(input())
    arr.append(num)
    n -= 1


odd1, odd2 = two_odd(arr)
print("The two odd-occurring numbers are:", odd1, "and", odd2)
