# -*- coding: utf-8 -*-

sehirler = ["Ankara", "İstanbul", "İzmir"]

for sehir in sehirler:
    if sehir == "İstanbul":
      #break                        # direk döngüyü kırar
      continue                      # döngünün o andakı geri kalan kısmını çağırmadan yeniden döngünün en başından başlar
    print(sehir)
    print("**********")