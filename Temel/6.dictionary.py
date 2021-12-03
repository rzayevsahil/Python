# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 03:22:18 2021

@author: Sahil
"""

# set'ler gibi sınırsız veri tutar
# günlük hayatdaki sözlükler gibi
# tanımı --> dictionary = {key:value,...} veya dict()


sozluk = { "book":"kitap", "table":"masa" }
sozluk2 = dict(kitap="book", masa="table")

print(sozluk)                   # {'book': 'kitap', 'table': 'masa'}
print(sozluk2)                  # {'kitap': 'book', 'masa': 'table'}



# BÖYLE BİŞEY YAZAMAYIZ!!!
# print(sözlük[0])



# anahtara göre değer bulma
print(sozluk["book"])           # kitap



# 1.eğer var olan anahtarın değerini değiştiryorsak, anahtar değeri güncellenir(1)
# 2.eğer olmayan anahtara değer atıyorsak, eleman dictionary'e eklenir(2)

# 1.anahtarın değerin değiştirmek
sozluk["book"] = "kitap1"
print(sozluk["book"])           # kitap1


# 2.yeni eleman ekleme
sozluk["pencil"] = "kalem"
print(sozluk)                   # {'book': 'kitap1', 'table': 'masa', 'pencil': 'kalem'}



# del() - sözlükden  key silmek
del(sozluk["book"])
print(sozluk)                   # {'table': 'masa', 'pencil': 'kalem'}



# len - uzunluk
print(len(sozluk))              # 2