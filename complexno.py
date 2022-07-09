#complex number
class complex:
    def getdata(self):
        self.real = input("enter the real part of the number \n")
        self.im = input("enter the imaginary part of the number \n")

    def add(self,type1,type2):
        self.real = type1.real +type2.real
        self.im = type1.im +type2.im

    def display(self):
        print("The complex number is "+str(self.real)+str("+")+str(self.im)+str("i"))


c1 = complex()
c2 = complex()
c1.getdata()
c2.getdata()
c3 = complex()
c3.add(c1,c2)
c3.display()
