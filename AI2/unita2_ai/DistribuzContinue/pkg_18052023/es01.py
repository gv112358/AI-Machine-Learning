"""Una variabile normale x ha media μ=50 e varianza σ2=64.
Calcola la probabilità che tale variabile sia compresa fra 30 e 60. """

import time
start = time.time()

import sys
sys.path.append("/home/studente26/IA 2/DistribuzContinue")
from Procedure.Estrazioni import ExNormale

fMu = 50
fSigma = 8
iNumProve = 10**5
fSuccessi = 0

for i in range(iNumProve):
    fRet = ExNormale(fMu,fSigma)
    if fRet > 30 and fRet < 60:
        fSuccessi += 1

print("La probabilità richiesta è: ", fSuccessi/iNumProve)

end = time.time()
print("Il tempo di esecuzione della procedura è: ", round(end-start,2))



