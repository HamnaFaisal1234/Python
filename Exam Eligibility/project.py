total_days = int(input("Enter the total number of working days : "))
absent_days = int(input("Enter the number of days absent : "))
present_days = total_days - absent_days
attendance_percentage = (present_days / total_days) * 100
print("Attendance Percentage: " + str(attendance_percentage) + "%")
if attendance_percentage < 75:
    print("You cannot sit for the exam due to low attendance.")
else:
    print("You can sit for the exam.")
