class sample :
    def set_name(self,  name):
        self.name=name
    def __add__(self, other):
        name=self.name+other.name
        return name




first_name=sample()
soncond_name=sample()

first_name.set_name("Favas ")
soncond_name.set_name("TP")
full_name=first_name+soncond_name
print(full_name)