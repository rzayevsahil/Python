# -*- coding: utf-8 -*-

# Soru: kullanıcının girdiği sayıya göre yıldız yapma


# Örnek:    girilen değer: 5

# çıktı
# *
# **
# ***
# ****
# *****



#-----------------------------------------------------------------------



sayi = int(input("Sayi giriniz : "))

yildiz = ""

for s in range(1,sayi+1):
    yildiz+="*"
    print(yildiz)