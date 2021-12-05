# -*- coding: utf-8 -*-

import matematikModule 

matematikModule.topla(5, 3)
matematikModule.carp(5, 3)



print("-----------------------------------")



import matematikModule as mm   #ismini mm olarak değiştiriyoruz

mm.topla(5, 3)
mm.carp(5, 3)
print(mm.customer["firstName"])



print("-----------------------------------")



from matematikModule import topla  #ismini mm olarak değiştiriyoruz

topla(5,3)