class Robot:
     def __init__(self , name):
          self.name = name
     def introduce(self):
            print(f"Hello, My name is {self.name}!")
Tom = Robot("Tom")
Jerry = Robot("Jerry")
Tom.introduce()
Jerry.introduce()
     
