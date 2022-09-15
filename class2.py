class Dog:
    # Class variable
    animal = "dog"
    
    # the __init__ method or constructor
    def __init__(self,breed,color):
        # instance variable
        self.breed=breed
        self.color=color
    # object of Dog class
Rodger = Dog("Pug", "brown")
Buzo = Dog("BullDog", "black")
print('Rodger details')
print('Rodger is a', Rodger.animal)
print('Breed: ',Rodger.breed)
print('Color: ',Rodger.color)

print('\nBuzo details: ')
print('Buzo is a', Buzo.animal)
print('Breed: ', Buzo.breed)
print('color: ', Buzo.color)