class First :
    def display_first(self):
        print('First')
class Second :
    def display_second(self):
        print("second")
class Third(First,Second):
    def display_third(self):
        print('third')

x=Third()
x.display_third()
x.display_first()
print(Third.mro())


