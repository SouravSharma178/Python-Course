#operator overloading
class student:
    def getdata(self):
        self.m1 = input("enter the m1 marks \n")
        self.m2 = input("enter the m2 marks \n")

    def display(self):
        print("This is the marks ",self.m1,self.m2)


    def add(self,obj1,obj2):
        self.m1 = obj1.m1 + obj2.m1
        self.m2 = obj1.m2 + obj2.m2
        print(self.m1,"+",self.m2)

s1 = student()
s2 = student()
s1.getdata()
s2.getdata()
s3 = student()
s3.add(s1,s2)






