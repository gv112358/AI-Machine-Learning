"""Ad un esame universitario, il voto medio è stato μ=24 con σ=4. Supponendo i voti normalmente distribuiti, calcolare la probabilità che uno studente abbia riportato:
A) Un voto superiore a 27
B) Un voto non inferiore a 22

E' inoltre, richiesto:

C) Il voto minimo riportato dal 70% degli studenti
D) Il voto massimo non superato dal 90% degli studenti """


import time
start = time.time()

import sys
sys.path.append("/home/studente26/IA 2/DistribuzContinue")
from Procedure.Estrazioni import ExNormale

fMu = 24
fSigma = 4
iNumProve = 10**6
lSuccessi = [0]*3
lRichieste = ["A", "B"]

for i in range(iNumProve):
    fRet = ExNormale(fMu,fSigma)
    if fRet > 27:
        lSuccessi[0] += 1
    if fRet >= 22:
        lSuccessi[1] += 1

for i in range(len(lRichieste)):

    print(f"La risposta alla richiesta {lRichieste[i]} è: {round(lSuccessi[i]*100/iNumProve,2)}%")

end = time.time()
print("Il tempo di esecuzione della procedura è: ", round(end-start,2))