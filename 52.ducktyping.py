#duck typing in python
class Duck:
    def sound(self):
        print("Quack Quack")

class Dog:
    def sound(self):
        print("Woof Woof")

class Cat:
    def sound(self):
        print("Meow Meow")

def All_sounds(obj):
    obj.sound()

x = Dog()
x.sound()
All_sounds(x)

