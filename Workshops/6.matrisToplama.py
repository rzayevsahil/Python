# -*- coding: utf-8 -*-

#Soru: matris toplamnı yapan kodu yazınız

#örnek

# 1.matris         2.matris         toplam matris
#  1 3 5            3 3 4            4  6  9
#  2 4 1      +     2 4 1      =     4  8  2
#  1 5 7            3 5 4            4  10 11

matris1 = [[1,3,5],[2,4,1],[1,5,7]]
matris2 = [[3,3,4],[2,4,1],[3,5,4]]

toplamMatris = [[0,0,0],[0,0,0],[0,0,0]]

for i in range(len(matris1)):
    for j in range(len(matris2)):
        toplamMatris [i][j] = matris1[i][j] + matris2[i][j]

print(toplamMatris)