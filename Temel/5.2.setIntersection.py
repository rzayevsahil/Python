# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 03:00:56 2021

@author: Sahil
"""

#----------------------------- Set Intersection -------------------------------


# Set Intersection --> yani her iki kümenin kesişimi

setA = {1,2,3,4,5}
setB = {1,3,4,6,7,8}

# 1.yöntem: set intersection --> & bu işaret demek
print(setA & setB)                  # {1, 3, 4}



# 2.yöntem: .intersection()
print(setA.intersection(setB))      # {1, 3, 4}
print(setB.intersection(setA))      # {1, 3, 4}