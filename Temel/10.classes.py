# -*- coding: utf-8 -*-

#%% Basics
class Matematik:
    #constructor
    def __init__(self):
        print("Çalıştı")
        
    def topla(self,sayi1,sayi2):
        return sayi1 + sayi2

    def cikar(self,sayi1,sayi2):
        return sayi1 - sayi2

    def carp(self,sayi1,sayi2):
        return sayi1 * sayi2

    def bol(self,sayi1,sayi2):
        return sayi1 / sayi2



# fonksiyon içinde "self" yazmadan kullanırsak:
    
# print("Toplam = " + str(matematik.topla(2,78)))
# "TypeError: topla() takes 2 positional arguments but 3 were given" hatası alırız

# print("Toplam = " + str(matematik.topla(2)))
# "TypeError: unsupported operand type(s) for +: 'Matematik' and 'int'" hatası alırız

# en son hatadan anladığım kadarıyla,
# self ---> class'ın referansına karşılık geliyor

matematik = Matematik()
print("Toplam = " + str(matematik.topla(2,78)))



#------------------------------------------------------------------------------

# constructor'da değer tanımlama
# self ---> this gibi bişey

class Matematik1:
    #constructor
    def __init__(self,sayi1,sayi2):
        self.sayi1 = sayi1
        self.sayi2 = sayi2
        
    def topla(self):
        #self.cikar()
        return self.sayi1 + self.sayi2

    def cikar(self):
        return self.sayi1 - self.sayi2

    def carp(self):
        return self.sayi1 * self.sayi2

    def bol(self):
        return self.sayi1 / self.sayi2

matematik1 = Matematik1(2,78)
print("Toplam = " + str(matematik1.topla()))



#------------------------------------------------------------------------------



#%% Property

#------------------------  özellik barındıran sınıflar  ------------------------


class Person:
    def __init__(self,firstName,lastName,age):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
        
person1 = Person("Sahil","Rzayev",22)
print(person1.firstName)



#------------------------  inheritance  ------------------------


class Worker(Person): # Person sınıfından miras alıyor
    def __init__(self,salary):
        self.salary = salary
        

        
class Customer(Person):
    def __init__(self,creditCardNumber):
        self.creditCardNumber = creditCardNumber
        
        
ahmet = Worker(55)
ahmet.age=22         # inheritance burada görülüyor