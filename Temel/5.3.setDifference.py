# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 03:02:02 2021

@author: Sahil
"""

#----------------------------- Set Difference -------------------------------


# Set Difference --> yani bir kümenin diğerinden farkı(a'nın b'den/b'nin a'dan farkı gibi)

setA = {1,2,3,4,5}
setB = {1,3,4,6,7,8}

# 1.yöntem: set difference --> - bu işaret demek
print(setA - setB)                  # {2, 5}
print(setB - setA)                  # {8, 6, 7}



# 2.yöntem: .difference()
print(setA.difference(setB))      # {2, 5}
print(setB.difference(setA))      # {8, 6, 7}