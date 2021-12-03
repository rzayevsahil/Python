# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 03:08:27 2021

@author: Sahil
"""

#----------------------------- Set Symmetric Difference -------------------------------


# Set Symmetric Difference --> yani bir kümenin diğerinden farkı birleşim kesişimi
# yani (a'nın b'den/b'nin a'dan farkı birleşim kesişim gibi) full a veya full b kısaca

setA = {1,2,3,4,5}
setB = {1,3,4,6,7,8}

# 1.yöntem: set symmetric difference --> ^ bu işaret demek
print(setA ^ setB)                  # {2, 5, 6, 7, 8}
print(setB ^ setA)                  # {2, 5, 6, 7, 8}



# 2.yöntem: .symmetric()
print(setA.symmetric_difference(setB))      # {2, 5, 6, 7, 8}
print(setB.symmetric_difference(setA))      # {2, 5, 6, 7, 8}