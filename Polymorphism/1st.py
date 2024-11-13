class Toyota :
    def __init__(self,speed, brand):
        self.speed = speed
        self.brand = brand
    def move(self):
        print("TOYOTA: It can move with a speed of 117mph")
class Tesla :
    def __init__(self,speed, brand):
        self.speed = speed
        self.brand = brand
    def move(self):
        print("TESLA: It can move with a speed of 250.0mph")
class BMW :
    def __init__(self,speed, brand):
        self.speed = speed
        self.brand = brand
    def move(self):
        print("BMW: It can move with a speed of 302mph")
Toyota1 = Toyota ("Sakichi toyoba" , "Toyota")
Tesla1 = Tesla ("Elon musk" , "Tesla")
BMW1 = BMW ("Stefam" , "BMW")
for x in (Toyota1 , Tesla1, BMW1):
    x.move()

        