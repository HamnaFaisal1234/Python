class Dad :
    def __init__(self,aggressive,eyes):
       self.aggressive=aggressive
       self.eyes=eyes
    def display(self):
        print(self.eyes,self.aggressive)
class son(Dad):
    def __init__(self,aggressive,eyes,age):
        self.age=age
        super(). __init__ (eyes,aggressive)
obj1=son("blue", "yes" ,10)
obj1.display() 


        


