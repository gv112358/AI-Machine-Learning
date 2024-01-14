"""L'altezza media di un gruppo di 20.000 individui è distribuita normalmente con media μ=170 cm e con deviazione standard σ=10 cm.
A) Qual è la probabilità che l'altezza sia compresa fra 155 e 180 cm.
B) Quante persone sono alte almeno 2 metri.
C) Quante persone sono alte non più di 1 metro e 60 cm."""

import time
start = time.time()

import sys
sys.path.append("/home/studente26/IA 2/DistribuzContinue")
from Procedure.Estrazioni import ExNormale

fMu = 170
fSigma = 10
iNumProve = 10**6
lSuccessi = [0]*3
lRichieste = ["A", "B", "C"]
lPopolazione = [1,20000,20000]


for i in range(iNumProve):
    fRet = ExNormale(fMu,fSigma)
    if fRet > 155 and fRet < 180:
        lSuccessi[0] += 1
    if fRet >= 200:
        lSuccessi[1] += 1
    if fRet <= 160:
        lSuccessi [2] += 1

for i in range(len(lRichieste)):

    print(f"La risposta alla richiesta {lRichieste[i]} è: ", round(lSuccessi[i]*lPopolazione[i]/iNumProve,3))


end = time.time()
print("Il tempo di esecuzione della procedura è: ", round(end-start,2))