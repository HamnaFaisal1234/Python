class Employee:
    def __init__(self):
        print("It is a Construction method")
    def __del__(self):
        print("It is a Destruction method")
obj = Employee()
del obj