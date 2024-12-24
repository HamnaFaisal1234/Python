largest_number = int(input("Enter largest number :"))
smallest_number = int(input("Enter smallest number :"))
num1 = largest_number
num2 = smallest_number
while smallest_number:
      number_store=smallest_number
      smallest_number=largest_number % smallest_number
      largest_number=number_store
print("HCF is", largest_number)
print("LCM is" , (num1 * num2) // largest_number)