class Animal:
    def speak(self):
        print("Animal Speaking")
# child dog inherit =s the base class animal
class Dog(Animal):
    def bark(self):
        print("Dog barking")
        # multilevel inheritence
class DogChild(Dog):
    def eat(self):
        print("Eating Bread")
d=DogChild()
d.bark()
d.speak()
d.eat()