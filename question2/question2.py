#Hi, I wrote this code by python lang

class Animal:   #creating main class Animal
    def speak(self):
        print("Animal sound")

class Dog(Animal):  #creating subclass Dog
    def speak(self):
        print("Woof!")

my_dog = Dog()     # Instantiate an object of Dog

my_dog.speak()     # Call the speak method of the Dog object
