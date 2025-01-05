bits=int(input('Enter a number:'))
binary_representation = bin(bits)[2:] 
print(binary_representation)
position = 1
while bits & 1 == 0:  
        bits = bits >> 1
        position += 1
print('Position of the first set bit:',position)   
