tupleListe = (2,4,6,"Ankara",(2,3,4),[])
liste = [2,4,6,"Ankara",[2,3,4],()]

print(type(tupleListe))     # <class 'tuple'>
print(type(liste))          # <class 'list'>

print(tupleListe)           # (2, 4, 6, 'Ankara', (2, 3, 4), [])
print(liste)                # [2, 4, 6, 'Ankara', [2, 3, 4], ()]

print(len(tupleListe))      # 6
print(len(liste))           # 6

# tuple - listelere benzer tek farkı tuple'yi değiştiremiyoruz!
#tupleListe[0] = 5          # TUPLE DEĞİŞTİRİLEMEZ!!!
liste[0] = 5
#print(tupleListe)          # KOD ÇALIŞMAZ!
print(liste)

# -2 sağdan ikinci elemanı gösterir
print(tupleListe[-2])       # (2, 3, 4)
print(liste[-2])            # [2, 3, 4]

# çıktıda sonunda otomatik olarak virgül koyar tuple
print(tupleListe[1:2])      # (4,)
print(liste[1:2])           # [4]

#--------------------------------------------------------------------------------                           

# değişkene "tek değer ataması" yaptığımız zaman değer sonuna "virgül" koymazsak,
# onu sıradan bir dizi/liste olarak tanımlar ve tipini de "str" olarak algılar
tupleDeger1 = ("Sahil")
print(tupleDeger1)              # Sahil
print(type(tupleDeger1))        # <class 'str'>

tupleDeger2 = ("Sahil",)
print(tupleDeger2)              # ('Sahil',)
print(type(tupleDeger2))        # <class 'tuple'>