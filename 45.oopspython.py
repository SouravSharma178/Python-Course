class computer:
    def __init__(self):
        self.name = "Sourav"
        self.age = 21
    def update(self):
        print("This will update age")
        self.name = "A"
        self.age  = 100
        print(self.name,self.age)
    def compare(self,other):
        if (self.age==other.age):
            return True
        else:
             return False


c1 = computer()
c2 = computer()

c1.update()
c2.update()
x  = c1.compare(c2)
print(x)

