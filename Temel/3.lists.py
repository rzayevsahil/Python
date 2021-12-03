ogrenci1 = "Engin"
ogrenci2 = "Sahil"
ogrenci3 = "Bilmem ne"

ogrenciler = [ogrenci1, ogrenci2, ogrenci3]
print(ogrenciler)



#append - listeye eleman ekleme
#remove - listeden eleman silmek
ogrenciler.append("Ahmet")
ogrenciler.remove(ogrenci3)
print(ogrenciler)



#list constructor
sehirler=list(("Ankara","İstanbul"))
print(sehirler)

#len - uzunluk belirtir
print(len(sehirler))



#diğer fonksiyonlar

#clear - listeyi temizler
#print(sehirler.clear())


#count("aranacak değer") - aranacak değerin listede var olan sayısını gösterir
print(sehirler.count("Ankara"))


#index - sırasını gösterir
print(sehirler.index("Ankara"))


#pop - index'i verilen değeri silme
sehirler.pop(1)
print(sehirler)


#insert - belirtilen index'e eleman yerleştirir
sehirler.insert(0, "Bakü")
print(sehirler)


#reverse - terse çevirir
sehirler.reverse()
print(sehirler)


#copy - koyalama işlemi yapar
sehirler3 = sehirler.copy()
print("sehirler3 --->" + str(sehirler3))


#dizileri yedekleme
sehirler2 = sehirler
sehirler2[0]="İzmir"
print(sehirler) #her ikisi aynı sonucu verir çünki her ikisi referans tipdir
print(sehirler2)


a=5
b=a
b=7
print(a) #5
print(b) #farklı sonucu verir #7 


#extend - birleştirir
sehirler.extend(sehirler3)
print(sehirler)


#sort - alfabetik veya sayısal olarak sıralar
sehirler.sort()
print(sehirler)
#bunun tersi
sehirler.reverse()
print(sehirler)
