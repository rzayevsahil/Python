# -*- coding: utf-8 -*-

sayilar = [1,2,3,4,5]

# sayilarKareli = []

# bunun yerine mapping kullanmak
# for sayi in sayilar:
#     sayilarKareli.append(sayi*sayi)



# x**2 = x*x - x'in karesi
sayilarKareli = list(map(lambda sayi : sayi**2, sayilar))

print(sayilarKareli)


#--------------------------------------------------------------------------


sayilarFiltreli = list(filter(lambda sayi : sayi>2, sayilar))

print(sayilarFiltreli) 


#--------------------------------------------------------------------------


from functools import reduce

sayilarFaktoriyel = reduce(lambda x,y : x*y, sayilar)

# çalışma mantığı :
#  x       y
#  1       2
#  1*2     3
#  2*3     4
#  6*4     5
#  24*5    end  ---> 120    

print(sayilarFaktoriyel)

