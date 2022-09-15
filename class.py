                            # class&object

# syntex to create a class

class MyClass:
    x=5
    
# creating object
# we access a class using (.)dot 
p1=MyClass()
print(p1.x)

class Dog:
#a simple class
# attributes
    attr1="mammal"
    attr2="dog"
    
Rodger=Dog()
print(Rodger.attr1)
print(Rodger.attr2)
                #                   __init__method
                
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
p1=Person("Johan",36)
print(p1.name)
print(p1.age)
                    