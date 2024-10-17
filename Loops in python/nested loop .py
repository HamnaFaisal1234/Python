# puthon program to star a pattern based on the number of rows by the user
n = int(input("Enter the number of rows;"))
for i in range (1,n+1):
  for j in range (i):print ("*" , end="" )
  print()
