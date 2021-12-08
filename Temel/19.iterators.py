# -*- coding: utf-8 -*-

sehirler = ["Ankara","İstanbul","İzmir","Van"]

iteratorum = iter(sehirler)

# arka arkaya çalıştırdığımızda listenin değerlerini tek tek gösterir
print(next(iteratorum))
print(next(iteratorum))
print(next(iteratorum))
print(next(iteratorum))

for sehir in sehirler:
    print(sehir)