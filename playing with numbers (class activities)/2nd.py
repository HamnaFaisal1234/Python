largest_number=int(input("Enter the largset number"))
smallest_number=int(input("Enter the smallest number"))
while smallest_number:
      number_store=smallest_number
      smallest_number=largest_number % smallest_number
      largest_number=number_store
print("HCF is", largest_number)