## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

# Dog is a Animal
class Dog(Animal):

    def __init__(self, name):
        ## Class Dog has a __init__ that taks parameters self and made
        self.name = name

    def doggy(self, Dog):
        test = 5
        print test

    def animales(self, Animal):
        testy = 4
        print testy
## Cat is a Animal
class Cat(Animal):


        ## Cat has a attribute name
        self.name = name

## Person is a object
class Person(object):

    def __init__(self, name):
        ## Person has a name of some kind
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

## ??
class Employee(Person):

    def __init__(self, name, salary):
        ## ?? Employee has a function named super that takes 
        super(Employee, self).__init__(name)
        ## Employee has a salary ammount
        self.salary = salary

## A Fish is a Object
class Fish(object):
    pass

## A Salmon is a FAish
class Salmon(Fish):
    pass

## A Halibut is a Fish
class Halibut(Fish):
    pass


rover = Dog("Rover")


satan = Cat("Satan")


mary = Person("Mary")

## ??
mary.pet = satan

## ??
frank = Employee("Frank", 120000)

## ??
frank.pet = rover

## ??
flipper = Fish()

## ??
crouse = Salmon()

## ??
harry = Halibut()