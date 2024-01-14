""" Da un'indagine su un campione di neonati, risulta che la distribuzione
dei pesi alla nascita è normale con media 3.2 con sigma 0.6 kg
A: quale percentuale presenta un peso alla nascita compreso tra 2.2 e 3.5
B: qual è il peso oltre il quale si trovano il 10% dei valori più elevati"""

import time
start = time.time()

import sys
sys.path.append("/home/studente26/IA 2/DistribuzContinue")
from Procedure.Estrazioni import ExNormale

fMu = 3.2
fSigma = 0.6
iNumProve = 10**6
iSuccessi = 0
lSuccessi = [0]*5

# entro 3.2 resta fuori il 50%
# 3.8 15.85%
# 4.4 2.275%
# 5 0.135% 
for i in range(iNumProve):
    fRet = ExNormale(fMu,fSigma)
    if fRet > 2.2  and fRet < 3.5:
        iSuccessi += 1
    if fRet >= 3.9:
        lSuccessi[0] += 1
    if fRet >= 4.0:
        lSuccessi[1] += 1
    if fRet >= 4.1:
        lSuccessi[2] += 1
    if fRet >= 4.2:
        lSuccessi[3] += 1
    if fRet >= 4.3:
        lSuccessi[4] += 1
    
    
print(f"La risposta alla richiesta A è: {round(iSuccessi*100/iNumProve,2)}%")
for i in range(len(lSuccessi)):
    print(f"Per {round(3.9 + i/10,2)} ottengo: {round(lSuccessi[i]*100/iNumProve,2)}%")



end = time.time()
print("Il tempo di esecuzione della procedura è: ", round(end-start,2))