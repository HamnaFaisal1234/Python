
A = 1  
B = 0
C = 1


step1 = A & B   
step2 = B & C   
step3 = step1 | step2  
step4 = ~step3 & 1  

Q = step3 | step4


print(f"Output (Q): {Q}")
