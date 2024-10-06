print ("                      Please enter numbers then it will show them in ascending order")
user_input = input ("'Enter values and also give space between values': ")
numbers = [int(num) for num in user_input.split()]
numbers.sort()
print ("here is an output!")
print ("Values in ascending order are" , numbers)