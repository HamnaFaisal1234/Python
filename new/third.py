def test(lst):
    result = {}
    for item in lst:
        result[item[0]] = item[1:]
    return result  

students = [[1, 'Hamna', 'XI'], [2, 'Aisha', 'XII'], [3, 'Ahsan', 'IX'], [4, 'Shreeman', 'IX'], [5, 'Ibrahim', 'V']]

print("\nOriginal list of lists:")
print(students)

print("\nConverted lists to a dictionary:")
print(test(students))




