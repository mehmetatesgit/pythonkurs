'''
#class

class Person:
    # class attributes
    address = 'no information'
    #constructor (yapıcı metod)
    def __init__(self, name, year):
        #object attribute
        self.name = name
        self.year = year
        # methods

    def intro (self):
        print('Hello There I am '+ self.name)

    def calculateAge(self):
        return 2020 - self.year

# object, instance



p1 = Person('Ali', 1997)
p2 = Person('ahmet',1987)

p1.intro()
p2.intro()

print(f"adım: {p1.name} yaşım: {p1.calculateAge()} ")
print(f"adım: {p2.name} yaşım: {p2.calculateAge()} ")

'''


class Circle:
    pi = 3.14
    
    def __init__(self, yaricap = 1):
        self.yaricap = yaricap
    
    def cevreHesapla(self):
        return 2 * self.pi * self.yaricap

    def alanHesapla(self):
        return self.pi * (self.yaricap**2)


c1 = Circle()
c2 = Circle(5)

print(f"c1: alan = {c1.alanHesapla()} çevre: {c1.cevreHesapla()} ")
print(f"c2: alan = {c2.alanHesapla()} çevre: {c2.cevreHesapla()} ")

