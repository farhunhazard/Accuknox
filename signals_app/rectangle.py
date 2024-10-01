class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width

    def __iter__(self):
        # Creating an iterator that first yields the length, then the width
        yield {'length': self.length}
        yield {'width': self.width}
    
    def area(self):
        return self.length*self.width

# Testing the Rectangle class
def test_rectangle():
    rect = Rectangle(10, 5)
    for attribute in rect:
        print(attribute)
    print(f"Area of Rectangle : {rect.area()}")

# Calling this function to test
if __name__ == "__main__":
    test_rectangle()
