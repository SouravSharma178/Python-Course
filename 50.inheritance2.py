#multiple inheritance
class A:
    def feature1(self):
        print("This is feature 1 of class A")

    def feature2(self):
        print("This is feature 2")

class B:
    def feature1(self):
        print("This is feature 1 of class B")
    def feature3(self):
        print("This is feature 3")

    def feature4(self):
        print("This is feature 4")

class C(A,B):
    def feature5(self):
        print("This is feature 5")

    def feature6(self):
        print("This is feature 6")

c1 = C()
c1.feature1()
c1.feature2()
c1.feature3()
c1.feature4()
c1.feature5()
c1.feature6()

