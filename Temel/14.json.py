# -*- coding: utf-8 -*-

import json


# Json datası tanımı
data = '{"firstName":"engin","lastName":"demiroğ"}'

# data'yı json tipine çevirdik
y = json.loads(data)

print(y["firstName"])
print(y["lastName"])



# json türünde olmayan veriyi jsonâ çevirme
customer = {
    "firstName" : "engin",
    "email" : "engindemirog@gmail.com"
    }

customerJson = json.dumps(customer)
print(customer)


# normal bir string'i json'a dönüştürme
print(json.dumps("Engin"))          # "Engin"
# sıradan bir string                # çıktılar arasındaki fark
print("Engin")                      # Engin