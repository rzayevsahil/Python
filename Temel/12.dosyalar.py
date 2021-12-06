# -*- coding: utf-8 -*-

# txt dosyası yoksa oluşturur (w-write)
# w - write     r - read        a - append(read and write)      
# x - create, direk oluştur demek eğer dosya varsa hata verir
# xt - text dosyası oluşturma

f = open("musteriler.txt")

for line in f:
    print(line)

f.close()

#print(f.read())                # dosya içeriğinin tamamını okuma

# print(f.read(10))             # dosya içeriğindeki ilk 10 karakteri oku
    
# print(f.readline())           # satır satır okuyor

# print(f.readline(10))         # dosya içeriğindeki ilk 10 karakteri oku



#-----------------------------------------------------------------------------



# default r(read)'dir
# append'de var olanın üzerine yazar
# write'da ise dosyanın üzerine yazar yani eski bilgileri kayb edersiniz

# fileToAppend = open("ogrenciler.txt","a")   # dosya oluşturuyor
fileToAppend = open("ogrenciler.txt","w")

fileToAppend.write("Engin")         # dosya içine yazma
fileToAppend.write("\n") 
fileToAppend.write("Sahil")

fileToAppend.close()
 


#-----------------------------------------------------------------------------


#%%
# dosya silme işlemi
import os

# os.remove("ogrenciler.txt")


if os.path.exists("ogrenciler.txt"):
    os.remove("ogrenciler.txt")
else:
    print("Dosya yok")
    
    

# klasörü tamamen silmek
os.rmdir("empty")