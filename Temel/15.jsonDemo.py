# -*- coding: utf-8 -*-

import json

# json dosyasını okumak için kullanılır ve okuma yaptıktan sonra dosya kendinden kapanıcaktır
with open("users.json") as users:
    
    # dosyayı okumak için "loads" değil de "load" kullanıyoruz
    data = json.load(users)
    
    for x in range(5):
        print(data[x]["username"])                  # ismi
        print(data[x]["email"])                     # mail adresi
        print(data[x]["address"]["street"])         # sokak
        print(data[x]["address"]["geo"]["lat"])     # kordinatlar
        print("--------------------------------")