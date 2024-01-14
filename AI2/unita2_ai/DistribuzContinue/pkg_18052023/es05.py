"""Se si suppone che una popolazione abbia il livello di acido urico (mg/100 ml)
segua una distribuzione gaussiana con media e deviazione standard risp
pari a 5.7 e 1 (mg/100 ml) si trovi la provabilità che un soggetto scelto
a caso abbia un livello di acido urico:

C:  trovare inoltre il valore di acido urico x tale che P(X>=x) = 0.40"""

import time
start = time.time()

import sys
sys.path.append("/home/studente26/IA 2/DistribuzContinue")
from Procedure.Estrazioni import ExNormale

fMu = 5.7
fSigma = 1
iNumProve = 10**6
lSuccessi = [0]*8

for i in range(iNumProve):
    fRet = ExNormale(fMu,fSigma)
    if fRet >= 5.8:
        lSuccessi[0] += 1
    if fRet >= 5.9:
        lSuccessi[1] += 1
    if fRet >= 6.0:
        lSuccessi[2] += 1
    if fRet >= 6.1:
        lSuccessi[3] += 1
    if fRet >= 6.2:
        lSuccessi[4] += 1
    if fRet >= 6.3:
        lSuccessi[5] += 1
    if fRet >= 6.4:
        lSuccessi[6] += 1
    if fRet >= 6.5:
        lSuccessi[7] += 1


for i in range(len(lSuccessi)):
    print(f"Per {round(5.8 + i/10,2)} ottengo: {round(lSuccessi[i]*100/iNumProve,2)}%")

end = time.time()
print(f"Il tempo di esecuzione della procedura è: {round(end-start,2)} secondi")