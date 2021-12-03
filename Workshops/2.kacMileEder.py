# -*- coding: utf-8 -*-

#Soru: kullanıcının girdiği km'nin kaç mile olduğunu hesapla

donusumOrani=0.621371192 
km = input("km giriniz: ")
mile=float(km)*donusumOrani 
print(str(km) + " km " + str(mile) + " mil eder")

