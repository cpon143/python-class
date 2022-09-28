# class Dog:
#     # Class variable
#     animal = "dog"
    
#     # the __init__ method or constructor
#     def __init__(self,breed,color):
#         # instance variable
#         self.breed=breed
#         self.color=color
#     # object of Dog class
# Rodger = Dog("Pug", "brown")
# Buzo = Dog("BullDog", "black")
# print('Rodger details')
# print('Rodger is a', Rodger.animal)
# print('Breed: ',Rodger.breed)
# print('Color: ',Rodger.color)

# print('\nBuzo details: ')
# print('Buzo is a', Buzo.animal)
# print('Breed: ', Buzo.breed)
# print('color: ', Buzo.color)

class Dog:
    # Class variable
    animal = "dog"

    # the inite method or constructer
    def __init__(self,breed):
        # instance variable
        self.breed=breed
    # add on instance variable
    def setColor(self,color):
        self.color=color
    # Retrives instance variable
    def getColor(self):
        return self.color
    # driver code
Rodger = Dog("Pug")
Rodger.setColor("brown")
print(Rodger.setColor)