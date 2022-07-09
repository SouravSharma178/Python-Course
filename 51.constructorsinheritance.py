#contructor in inheritance
class A:
    def __init__(self):
        print("This is A cons")
    def feature1(self):
        print("This is feature 1")

    def feature2(self):
        print("This is feature 2")

class B:
    def __init__(self):
        self.age = 50
        print("This is B cons")
        print(self.age)
    def feature2(self):
        print("This is feature 2 of class B")

    def feature4(self):
        print("This is feature 4")
#it calls the constructor of the class  which is to the right first
class C(B,A):
    def __init__(self):
        # super().__init__()
        print("This is C cons")
    def feature5(self):
        print("This is feature 5")

    def feature6(self):
        print("This is feature 6")

    # def feat(self):
    #     super().feature2()


c1 = C()
# c1.feat()

