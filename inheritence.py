class Animal:
    def speak(self):
        print("Animal Speaking")
# child dog inherit =s the base class animal
class Dog(Animal):
    def bark(self):
        print("Dog barking")
d=Dog()
d.bark()
d.speak()