#class variables vs instance variables
#if a class variable is changed then it changes for all values
class car:
    wheels = 4
    def __init__(self,brand,mileage):
        self.brand = brand
        self.mileage = mileage
    def display(self):
        self.brand = "Ferrari"
        self.mileage = 10
        print("This is the detail ",self.brand,self.mileage)

c1 = car("bmw",21)
c2 = car("Tata",55)
#to change the data for a class variable we use the class.class variable
c1.wheels = 5
print(c1.wheels,c2.wheels)
print(c1.brand,c1.mileage)
print(c2.brand,c2.mileage)
c2.display()
print(c2.brand)
print(c2.mileage)





