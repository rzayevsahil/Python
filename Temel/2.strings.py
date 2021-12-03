# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 14:51:08 2021

@author: Sahil
"""

#substring
mesaj = "Merhaba dünya"
yeniMesaj=mesaj[2:5]
yeniMesaj1=mesaj[:2]
yeniMesaj2=mesaj[2:]
print(yeniMesaj)
print(yeniMesaj1)
print(yeniMesaj2)



#len - uzunluk
sonHarf=mesaj[len(mesaj)-1:len(mesaj)]
print(len(mesaj))
print(sonHarf)



#lower upper
print(mesaj.upper())
print(mesaj.lower())



#replace - değiştirir
print(mesaj.replace("ü", "u"))



#split - kelime kelime parçalara ayırır
#strip - boşlukları atar
bilgi="      Sahil Rzayev Bakü ".strip()
bilgi1="      Sahil Rzayev Bakü "
bilgi3="      Sahil;Rzayev;Bakü ".strip()
print(bilgi.split())
print(bilgi1.split(" "))
print(bilgi3.split(";")[2])



#input
ad=input("Adınız?")
sayi1=input("Sayi1 = ")
sayi2=input("Sayi2 = ")
print(int(sayi1)+int(sayi2))