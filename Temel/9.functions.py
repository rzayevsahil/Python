# -*- coding: utf-8 -*-

#%%
sehir = "Ankara"

print(sehir.upper())
print(sehir.endswith("a"))

#%%
def selamVer(isim = "default bir isim"):
    print("Merhaba " + str(isim).upper())
    
selamVer()
selamVer("sahil")



def selamVer2(isim, soyisim = " default soyisim"):
    print("Merhaba " + isim + " " + soyisim)
    
selamVer2("Sahil")          # default değeri sonda ver ki sıkıntı çıkmasın
selamVer2("Sahil","Rzayev")
#%%


# return eden fonksiyonlar


def dikUcgenAlaniHesapla(a,b):
    return a*b/2

alan = dikUcgenAlaniHesapla(2, 3)
print(alan)



# Lambda - tek satırda yazılır, yoksa çalışmaz ve hata verir
dikUcgenAlaniHesapla2 = lambda a,b : a*b/2 
print(dikUcgenAlaniHesapla2(2,3))



x=dikUcgenAlaniHesapla2
print(x(4,5))