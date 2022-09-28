class Calculation1:
    def Summation(self,a,b):
        return a+b;
class Calculation2:
    def Multiplication(self,a,b):
        return a*b;
class Drived(Calculation1,Calculation2):
    def Divided(self,a,b):
        return a/b;
d=Drived()
print("Summation a+b= ",d.Summation(10,20))
print("Multiplicatin a*b= ",d.Multiplication(10,20))
print("Division a/b= ",d.Divided(10,20))