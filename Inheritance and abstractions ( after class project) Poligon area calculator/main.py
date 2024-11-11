
class GeometryShape:
    def __init__(self, name):
        self.name = name  

    def area(self):
        
        raise NotImplementedError("This method should be overridden in a subclass")

    def perimeter(self):
        raise NotImplementedError("This method should be overridden in a subclass")

    def display(self):
       
        print(f"Shape: {self.name}")
        print(f"Area: {self.area()}")
        print(f"Perimeter: {self.perimeter()}")

class Rectangle(GeometryShape):
    def __init__(self, length, width):
        super().__init__("Rectangle") 
        self.length = length
        self.width = width

    def area(self):
       
        return self.length * self.width

    def perimeter(self):
        
        return 2 * (self.length + self.width)


class Square(GeometryShape):
    def __init__(self, side):
        super().__init__("Square")  
        self.side = side

   
    def area(self):
       
        return self.side * self.side

    def perimeter(self):
        
        return 4 * self.side


if __name__ == "__main__":
    
    rect = Rectangle(5, 10)
    rect.display() 

    print("\n---\n")

    
    sq = Square(4)
    sq.display()

