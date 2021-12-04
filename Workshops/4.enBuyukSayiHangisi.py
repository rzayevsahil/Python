# -*- coding: utf-8 -*-

#Soru: kullanıcıdan 3 tane sayı istiyoruz. En büyük sayı hangisi ise onu ekrana yazdırıyoruz

sayi1 = int(input("1.sayi giriniz: "))
sayi2 = int(input("2.sayi giriniz: "))
sayi3 = int(input("3.sayi giriniz: "))

if (sayi1 >= sayi2) and (sayi1 >= sayi3):
    enBuyuk = sayi1
elif (sayi2 >= sayi1) and (sayi2 >= sayi3):
    enBuyuk = sayi2
else:
    enBuyuk = sayi3

print("En büyük sayı : " + str(enBuyuk))
print("En büyük sayı :",enBuyuk) # artı(+) yerine virgül(,) de kullana biliriz - aynı şey yani