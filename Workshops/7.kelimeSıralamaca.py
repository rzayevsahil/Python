# -*- coding: utf-8 -*-

#Soru: kullanıcı bir cümle yazıyor ve o cümledeki kelimeleri sırasıyla alt alta yazdır

# örnek :
# cümle = "Bugün hava çok güzel"

# çıktı :
#   Bugün
#   hava
#   çok
#   güzel



cumle = "Bugün hava çok güzel"

kelimeler = cumle.split()
kelimeler.sort()

for kelime in kelimeler:
    print(kelime)