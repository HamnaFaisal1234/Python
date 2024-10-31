#Write a program to create a class with name Student and perform the following tasks - Create a class variable grade and name Create a function to print a sentence Create a function to print class variables grade and name Create an object of class Student Call the two functions to execute them
class student:
   def __init__(self, name, grade):
        self.name=name
        self.grade=grade
   def display(self):
        print("My name is", self.name,"\n" , "My grade is", self.grade)
obj1=student("Hamna",10)
obj1.display()




