# -*- coding: utf-8 -*-

# Soru: kullanıcı sayı girdiğinde onun asal olup olmadığını bulan kodu yazınız

sayi = int(input("Sayi giriniz : "))
sayac = 0

# benim yaptığım

for s in range(2,sayi): 
    if sayi % s == 0:
        sayac+=1
if sayac==0 and sayi != 1:
    print("Asaldır")
elif sayac!=0 and sayi != 1:
    print("Asal değildir")
else:
    print("hiçbişey")
    
    
    
# -----------------------------------------------



# hocanın yaptığı

sayi1 = int(input("Sayi giriniz : "))
asalMi = True
for x in range(2,sayi):
    if sayi % x == 0:
        asalMi = False
        break
    
if asalMi == True:
    print("ASAL")
else:
    print("ASAL DEĞİL")



