from abc import ABC, abstractmethod


class Animal(ABC):

    def __main__(self):
        print(f"Class Animal is an abstract class that has abstract method move \n" +
              f"Method move is an abstract method of an abstract class Animal\n"
              f"=== Below is the oupput of the code ===")

    def move(self):
        pass


class Human(Animal):

    def move(self):
        print("I can walk and run")


class Snake(Animal):

    def move(self):
        print("I can crawl")


class Dog(Animal):

    def move(self):
        print("I can bark")


# Driver code
R = Animal()
R.__main__()

R = Human()
R.move()

K = Snake()
K.move()

R = Dog()
R.move()
