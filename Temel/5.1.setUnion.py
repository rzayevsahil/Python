# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 02:37:27 2021

@author: Sahil
"""

#----------------------------- Set Union -------------------------------


# Set Union --> yani her iki kümenin birleşimi

setA = {1,2,3,4,5}
setB = {1,3,4,6,7,8}

# 1.yöntem: set union --> | bu işaret demek
print(setA | setB)                  # {1, 2, 3, 4, 5, 6, 7, 8}



# 2.yöntem: .union()
print(setA.union(setB))             # {1, 2, 3, 4, 5, 6, 7, 8}
print(setB.union(setA))             # {1, 2, 3, 4, 5, 6, 7, 8}