

class Human:
    """docstring for Human"""
    
    def __init__(self, name,age,gender):
        
        self.name = name
        self.age = age
        self.gender = gender

    def print_human(self):
        print self.name
        print self.age
        print self.gender

a = Human('Jony Roy', 26, 'Male')
#print a.name,'\n', a.age, '\n', a.gender,'\n'
a.print_human()

b = Human()
b.print_human()