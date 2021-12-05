# -*- coding: utf-8 -*-

#Soru: girilen değerin matrisini bulan kodu yazınız

sayi = int(input("Sayı giriniz : "))
faktoriyel = 1;

if sayi<0:
    print("Negatif sayıların faktoriyeli hesaplanamaz!!!")
elif sayi==0:
    print("Sonuç : 0")
else:
    for s in range(1,sayi+1):
        faktoriyel*=s
    # print("Sonuç : " + str(faktoriyel))
    print("Sonuç :",faktoriyel)
    
