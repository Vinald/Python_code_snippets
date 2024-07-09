class Student():
    def __init__(self, name='Name', house='House'):
        self.name = name
        self.house = house 
        
    # Prints an object in a formatted way
    def __str__(self):
        return f'{self.name} stays in {self.house}'
    
    @classmethod
    def get(cls):
        name = input('Name: ')
        house = input('House: ')
        return cls(name, house)
    
    # getter
    @property
    def house(self):
        return self._house
    
    # setter
    @house.setter
    def house(self, house):
        if house not in ['seeta', 'mukono', 'kireka']:
            raise ValueError('Invalid house')
        self._house = house
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError('Name Required')
        self._name = name



def main():
    student = Student.get()
    print(student)


if __name__ == '__main__':
    main()

    