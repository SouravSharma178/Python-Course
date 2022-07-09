#oops python
class Computer:
    #this is the constructor
    def __init__(self,name):
        self.name = name
        print("This is the class")
    def config(self):
      print("This is the config",self.name)

comp1 = Computer("sourav")
comp1.config()
