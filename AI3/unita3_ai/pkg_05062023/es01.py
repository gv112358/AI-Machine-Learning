""" indipendentemente dal processo generatore, la media delle medie è gaussiana
Date quattro distribuzioni: Gauss, uniforme, Poisson, Chi-quadro, mostriamo
empiricamente l'affermazione precedente """ 

import time
start = time.time()
import numpy
import sys
sys.path.append("/home/studente26/IA 3")
#sys.path.append("C:\\Users\giov\\Desktop\\Code\\IA 3")
from Procedure.Estrazioni import ExNormale, ExUniforme, ExPoisson, ExChiQuadro
import matplotlib.pyplot as plt

#estrazioni uniformi
a = 5
b = 12
iSampleDim = 20

iNumProve = 10**4

def Classifica(fValue,min,max):
    for i in range(int(max-min)):
        if fValue >= min and fValue <min + i:
            return min + i + 0.5

def Classifica1(fValue):
    fParteDecimale = fValue - int(fValue)
    if fParteDecimale>=0.5:
        return int(fValue) + 1
    return int(fValue)
    

x =[0]*iSampleDim #lista estratti
medie = [0]*iNumProve #lista medie
for j in range(iNumProve):
    for i in range(iSampleDim):
        x[i] = ExUniforme(a,b)
    medie[j] = sum(x)/iSampleDim
    #medie[j] = Classifica(medie[j], a, b)
    medie[j] = Classifica1(medie[j])
    

    

end = time.time()
print(f"Il tempo di esecuzione della procedura è: {round(end-start,2)} sec "  )

plt.hist(medie)
plt.show()




