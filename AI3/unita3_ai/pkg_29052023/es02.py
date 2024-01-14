
"""Dato N(8,6), calcolare le code rispetto a :
- 16.3
- 3.4"""

import time
start = time.time()

import sys
sys.path.append("/home/studente26/IA 3")
#sys.path.append("C:\\Users\giov\\Desktop\\Code\\IA 3")
from Procedure.Estrazioni import ExNormale
from math import sqrt

fMu = 8
fSigma = 6
iNumProve = 10**6

code = [0]*2
Xvalue1 = 3.4
Xvalue2 = 16.3

for i in range(iNumProve):
    Ret = ExNormale(fMu, fSigma)
    if Ret > 16.3:
        code[1] += 1
    if Ret < 3.4:
        code[0] += 1

for i in range(2):
    print(f"la lunghezza della code è: {round(code[i]/iNumProve,2)}")

#oppure usando la procedura creata in Estrazioni

end = time.time()
print("Il tempo di esecuzione della procedura è: ", round(end-start,2))
