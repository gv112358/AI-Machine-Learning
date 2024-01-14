"""Es4 unimib"""

import sys
sys.path.append("/home/studente26/IA 2/DistribuzContinue")
from Procedure.Estrazioni import ExNormale
from math import sqrt

fMu1 = 7.6
fSigma1 = sqrt(0.9)
fMu2 = 9.6
fSigma2 = 1.0
iNumProve = 10**6
iSuccessi1 = 0
iSuccessi2 = 0
iGrNI = 0
iGrI = 0

for i in range(iNumProve):
    fRet1 = ExNormale(fMu1,fSigma1)
    if fRet1 > 9.4  and fRet1 < 9.6:
        iSuccessi1 += 1
    if fRet1 > 7.6  and fRet1 < 9.4:
        iSuccessi2 += 1
    fRet2 = ExNormale(fMu2, fSigma2)
    if fRet1 > 9.0:
        iGrNI += 1
    if fRet2 > 9.0:
        iGrI += 1

print(f"la richiesta A: {round(iSuccessi1*100/iNumProve,2)}%")
print(f"la richiesta B: {round(iSuccessi2*100/iNumProve,2)}%")
print(f"la richiesta C: {round(0.2*(iGrI + iGrNI)/iNumProve,2)} ")


    

