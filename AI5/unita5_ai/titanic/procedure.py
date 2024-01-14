import sys
from math import sqrt
def distanza_euclidea(row1,row2):
    print(row1)
    print("\n")
    print(row2)
    sys.exit()
    somma = 0.0
    for i in range(len(row1)):
        somma += (row1[i] - row2[i])**2
    return sqrt(somma)


def distanza_new(row1,row2):
    somma = 0.0
    for i in range(len(row1)):
        somma += (row1[i] - row2[i])**2
    return sqrt(somma)



