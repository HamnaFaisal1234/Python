class Computer :
    def __init__(self):
        self.__maxprice = 1000
    def sell(self):
        print("Selling price : {}".format(self.__maxprice)) 
    def setMaxPrice(self , price):
        self.__maxprice = price
Obj1= Computer()
Obj1.sell()
Obj1.setMaxPrice(500)
Obj1.sell()
