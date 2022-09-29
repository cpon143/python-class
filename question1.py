# create a class building having properties like name , area create another class like apartment inheriting the properties
# of building. Also create instance of it
class building:
    def properties(self,name,area):
        self.name=name
        self.area=area
class apartment(building):
    