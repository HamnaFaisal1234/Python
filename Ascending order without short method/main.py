list = [5, 3, 6, 9, 1, 7, 4]
for i in range(len(list)):
    for j in range(len(list) - i - 1):
        if list[j] < list[j + 1]:  
            list[j], list[j + 1] = list[j + 1], list[j]  
print("Ascending Order:", list)