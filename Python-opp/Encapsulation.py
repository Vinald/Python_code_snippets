# private variables
# Private variables are those variables that should neither be accessed outside the class nor by any base class.
class Area:
    def __init__(self):
        self.__height = 0
        self.__width = 0
        self.__area = 0
    
    def set_height(self, height):
        self.__height = height
    
    def set_width(self, width):
        self.__width = width
    
    def get_area(self):
        self.__area = self.__height * self.__width
        return self.__area
    
    def __repr__(self):
        return f"Height: {self.__height}, Width: {self.__width}, Area: {self.__area}"


a = Area()
a.set_height(5)
a.set_width(6)
print(a.get_area())
print(a)


# private methods
# Private methods are those methods that should neither be accessed outside the class nor by any base class.

class Area:
    def __init__(self):
        self.__height = 0
        self.__width = 0
        self.__area = 0
    
    def __calculate_area(self):
        self.__area = self.__height * self.__width
    
    def set_height(self, height):
        self.__height = height
    
    def set_width(self, width):
        self.__width = width
    
    def get_area(self):
        self.__calculate_area()
        return self.__area
    
    def __repr__(self):
        return f"Height: {self.__height}, Width: {self.__width}, Area: {self.__area}"


a = Area()
a.set_height(5)
a.set_width(6)
print(a.get_area())
print(a)
