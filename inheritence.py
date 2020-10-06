class BaseClass:
    def __init__(self) -> object:
        print("base init function")
    def set_name(self,name):
        self.name=name

class SubClass(BaseClass ):
    def __init__(self):
        super().__init__()
        print("Subclass init ")
    def welcome(selfj):
        print("welome")

    def display_name(self):
        super().set_name("aydin")
        print("Name :"+self.name)

y=SubClass()
y.welcome()
y.set_name("Favas")
y.display_name()
