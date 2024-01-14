"""Se si suppone che una popolazione abbia il livello di acido urico (mg/100 ml)
segua una distribuzione gaussiana con media e deviazione standard risp
pari a 5.7 e 1 (mg/100 ml) si trovi la provabilità che un soggetto scelto
a caso abbia un livello di acido urico:
A: minore di 4.9 mg/100ml
B: compreso tra 4.9 e 6.2 
C:  trovare inoltre il valore di acido urico x tale che P(X>=x) = 0.40"""

import time
start = time.time()

import sys
sys.path.append("/home/studente26/IA 2/DistribuzContinue")
from Procedure.Estrazioni import ExNormale

fMu = 5.7
fSigma = 1
iNumProve = 10**6
lSuccessi = [0]*2
lRichieste = ["A", "B"]

for i in range(iNumProve):
    fRet = ExNormale(fMu,fSigma)
    if fRet < 4.9:
        lSuccessi[0] += 1
    if fRet > 4.9  and fRet < 6.2:
        lSuccessi[1] += 1
    

for i in range(len(lRichieste)):
    print(f"La risposta alla richiesta {lRichieste[i]} è: {round(lSuccessi[i]*100/iNumProve,2)}%")

end = time.time()
print("Il tempo di esecuzione della procedura è: ", round(end-start,2))