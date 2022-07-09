#types of methods in python
#1.Class methods 2.instance methods 3.static methods(that do not need any object)
class student:
    school = "ryan"
    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
    def avg(self):
        return ((self.m1+self.m2+self.m3)/3)

    def set_m1(self,value):
        self.m1 = value
    def get_m1(self):
        return self.m1

    @classmethod
    def display1(cls):
        return cls.school

    #static methods
    @staticmethod
    def info():
        print("This is the static method")

s1 = student(47,53,60)
x = s1.avg()
print(x)
y = s1.set_m1(50)
z = s1.avg()
print(z)
q = student.display1()
print(q)
student.info()




