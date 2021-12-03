# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 00:28:16 2021

@author: Sahil
"""

# belirli bir algoritmaya göre sıralar
# index'siz ve sırasız elemanlardan oluşur
# veri tekrarı olamaz - unique(eşsiz)

# studentsSet2 = set("Mehmet","Veli","Ayşe")  # böyle de tanımlaya biliriz

studentsSet = {"Engin","Derin","Salih","Ahmet"}
print(studentsSet)                  # {'Salih', 'Engin', 'Ahmet', 'Derin'}
 


for student in studentsSet:
    print(student)                  # Salih
                                    # Engin
                                    # Ahmet
                                    # Derin



# true yada false döner
print("derin" in studentsSet)       # False
print("Derin" in studentsSet)       # True



if "Derin" in studentsSet:
    print("Listede var")            # Listede var
    


# ekleme
studentsSet.add("Ali")
print(studentsSet)                  # {'Salih', 'Ali', 'Ahmet', 'Engin', 'Derin'}



studentsSet.update(["Merve","Mert","Selin"])
print(studentsSet)                  # {'Salih', 'Ali', 'Merve', 'Mert', 'Ahmet', 'Selin', 'Engin', 'Derin'}



# len - uzunluk
print(len(studentsSet))



# remove - silme
studentsSet.remove("Selin")
print(studentsSet)                  # {'Salih', 'Ali', 'Merve', 'Mert', 'Ahmet', 'Engin', 'Derin'}
print(len(studentsSet))             # 7



# remove peş peşe yazsak elemanı sildiği için yeniden o elemanı silmeye çalıştığında
# elemanı bulamadığı için hata verir. hata vermesin diye "discard" kullanıyoruz
studentsSet.discard("Selin")
print(studentsSet)  
print(len(studentsSet))             # 7



# pop -  ilk elemanı siler
x = studentsSet.pop()
print(x)                            # Salih
print(studentsSet)                  # {'Ali', 'Merve', 'Mert', 'Ahmet', 'Engin', 'Derin'}



# clear - tüm içeriğini temizler
studentsSet.clear()
print(studentsSet)                  # set()
print(len(studentsSet))             # 0



#   del - set'in kendisini silmek
del studentsSet
print(studentsSet)                  # NameError: name 'studentsSet' is not defined