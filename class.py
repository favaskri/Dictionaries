class MySamplClass:
    year=2020
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def add_age(self):
        self.age=self.age+1
    def relocate(self,place):
        self.place=place
    def display(self):
        print("year"+str(MySamplClass.year))
        print("Name:"+self.name,"\nage :"+str(self.age),"\nPlace :"+self.place)

    @classmethod
    def add_year(cls):
       cls.year = cls.year + 1
    @staticmethod
    def display_welcome():
        print("welcome")

       # print("hello")
    #def hello(self,n):
       # self.name=n

   # def print_name(self):
        #print(self.name)


MySamplClass.display_welcome()
x=MySamplClass("favas",32,"karlai")
y=MySamplClass("shina",24,"nilambur")
x.display()
y.display()

print("----------------------------")
x.add_age()
y.add_age()
x.display()
y.display()
print("------------------------------")
MySamplClass.add_year()
x.add_age()
y.add_age()
x.display()
y.display()
print("---------------")

x.relocate("bangalore")
y.relocate("bangalore")
x.add_age()
x.add_age()
x.display()
y.display()



#name='favas'
#x.hello(name)
#y.hello('aydin')
#x.print_name()
#y.print_name()
