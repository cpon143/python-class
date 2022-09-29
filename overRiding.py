class Cumpute:
    def area(self, x=None, y=None):
        if x!=None and y!=None:
            return x*y
        elif x!=None:
            return x*x
        else:
            return 0
obj=Cumpute()
obj.area()
obj.area(6)
obj.area(2,8)

# --------------------------------------------------------------------------

class Shape:
    data1="abc"
    def no_of_sides(self):
        print("My sides need to be decided I am a free from shape")
    def twoD(self):
        print('I am 2D object')
class Square(Shape):
    data1='abc'
    def no_of_sides(self):
        print("I have some data")
    def Color(self):
        print("Anything")
sq=Square()
print(sq.no_of_sides())
print(sq.twoD())
print(sq.Color())

# --------------------------------------------------------------------------

class Employee:
    def workinghrs(self):
        self.hrs=50
        
    def printhrs(self):
        print("Total working hrs : ",self.hrs)
        
class Trainee(Employee):
    def workinghrs(self):
        self.hrs=60
        
    def resothrs(self):
        super().workinghrs()
employee=Employee()
employee.workinghrs()
employee.printhrs()

trainee=Trainee()
trainee.workinghrs()
trainee.printhrs()
trainee.resothrs()

# -------------------------------------------------------

class Solution:
    __privateCounter=0
    def sum(self):
        self.__privateCounter+=1
        print(self.__privateCounter)
count=Solution()
count.sum()
count.sum()

# here we have accessed the private date
# member through class name

print(count._Solution__privateCounter)





