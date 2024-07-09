# Parent class representing an Animal
class Animal:
    alive = True
    
    def eat(self):
        print('eating')

    def sleep(self):
        print('sleeping')


# Child class inheriting from Animal class
class Rabbit(Animal):
    print('Rabbit')


# Child class inheriting from Animal class
class Fish(Animal):
    print('Fish')


rabbit1 = Rabbit()
fish1 = Fish()
rabbit1.eat()
print(rabbit1.alive)


# Parent class representing an Organism
class Organism:
    alive = True


# Child class inheriting from Organism class
class Animal(Organism):
    def eat(self):
        print('all animals eat')


# Child class inheriting from Animal class
class Dog(Animal):
    def bark(self):
        print('all dogs bark')


dog1 = Dog()
print(dog1.alive)
dog1.bark()
dog1.eat()


# Parent class representing an Organism
class Organism:
    alive = True


# Child class inheriting from Organism class
class Animal(Organism):
    def eat(self):
        print('all animals eat')
        return self


# Child class inheriting from Animal class
class Dog(Animal):
    def bark(self):
        print('all dogs bark')
        return self


dog1 = Dog()
print(dog1.alive)
dog1.bark().eat()

dog2 = Dog()
print(dog2.alive)
dog2.bark().eat()


# Parent classes representing Prey and Predator
class Prey:
    def prey(self):
        print('prey')


class Predator:
    def predator(self):
        print('The animal kills.')


# Child class inheriting from both Prey and Predator classes
class Animal(Predator, Prey):
    def animal(self):
        print('an animal may be either a prey or a predator or both.')


# Child class inheriting from Animal, Predator, and Prey classes
class Fish(Animal, Predator, Prey):
    def fish(self):
        print('fish is both a predator and prey.')


fish1 = Fish()
fish1.prey()
fish1.animal()

fish2 = Fish()
fish2.prey()
fish2.predator()


# Class representing a Triangle
class Triangle:
    def __init__(self, sides):
        self.sides = sides

    def gperimeter(self):
        perimeter = sum(self.sides)
        return perimeter


print(' |\\ ')
print(' | \\ ')
print('a|  \\ b')
print(' |   \\ ')
print(' |____\\')
print('     a    ')

a = int(input('Enter the value for side a: '))
b = int(input('Enter the value for side b: '))
c = int(input('Enter the value for side c: '))

perimeter1 = Triangle([a, b, c])
perimeter = perimeter1.gperimeter()
print('The perimeter is', perimeter)


# Parent class representing an Animal
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print('Animal speaks')


# Child class inheriting from Animal class
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def speak(self):
        print('Dog barks')


dog1 = Dog('Tommy', 'German Shepherd')
dog1.speak()
print(dog1.name)
print(dog1.breed)
