# Step 1: Overwrite or write new content to the file
file = open('students.txt', 'w')
file.write("Alice, Math, Alice's favorite subject is Math.\n")
file.write("Bob, Science, Bob's favorite subject is Science.\n")
file.close()

# Step 2: Append additional content to the file
file = open('students.txt', 'a')
file.write("Charlie, History, Charlie's favorite subject is History.\n")
file.close()

# Step 3: Read content from the file
file = open('students.txt', 'r')
content = file.read()
print("Content of 'students.txt' before modifications:\n", content)
file.close()

# Step 4: Create or update student records
new_name = input("Enter the name of the student to update or add: ")
new_subject = input("Enter the favorite subject: ")

# Read current content
file = open('students.txt', 'r')
records = file.readlines()
file.close()

# Update or add record
updated = False
for i in range(len(records)):
    if records[i].startswith(new_name + ","):
        records[i] = f"{new_name}, {new_subject}, {new_name}'s favorite subject is {new_subject}.\n"
        updated = True
        break
if not updated:
    records.append(f"{new_name}, {new_subject}, {new_name}'s favorite subject is {new_subject}.\n")
# Write updated content back to the file
file = open('students.txt', 'w')
file.writelines(records)
file.close()

# Step 5: Read and display updated content
file = open('students.txt', 'r')
updated_content = file.read()
print("\nContent of 'students.txt' after modifications:\n", updated_content)
file.close()

# Step 6: Count and display the number of records (lines)
file = open('students.txt', 'r')
Counter = 0
Content = file.read()
CoList = Content.split("\n")
for i in CoList:
    if i:
        Counter += 1
print("\nThis is the number of records in the file:", Counter)
file.close()
