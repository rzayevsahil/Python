# -*- coding: utf-8 -*-

#Soru: girilen sayının pozitif yoksa negatif mi olduğunu bulan kodu yazınız

sayi=int(input("Sayi giriniz: "))

if sayi < 0:
    print("Negatif")
elif sayi == 0:
    print("Sıfır")
else:
    print("Pozitif")

