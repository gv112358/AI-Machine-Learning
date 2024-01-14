"""Provare che la media di una variabile normale è una normale con stessa media e sigma_media = sigma/sqrt(c) dove c è la numerosità campionaria"""
import time
start = time.time()

import sys
sys.path.append("/home/studente26/IA 3")
#sys.path.append("C:\\Users\giov\\Desktop\\Code\\IA 3")
from Procedure.Estrazioni import ExNormale
from math import sqrt

fMu = 10
fSigma = 4.5
iNumProve = 10**4

c = 100 # numerosità campionaria

x = [0]*c
x_media = 0
fMu_media = fMu
fSigma_media = fSigma/sqrt(c)

iFreqIntervallo = [0]*3
prob = [0]*3

for j in range(iNumProve):
        for i in range(c):
            x[i] = ExNormale(fMu, fSigma)
        x_media = sum(x)/c
    
        if x_media >= (fMu_media - fSigma_media) and x_media <= (fMu_media + fSigma_media):
            iFreqIntervallo[0] += 1
        if x_media >= (fMu_media - fSigma_media*2) and x_media <= (fMu_media + fSigma_media*2):
            iFreqIntervallo[1] += 1
        if x_media >= (fMu_media - fSigma_media*3) and x_media <= (fMu_media + fSigma_media*3):
            iFreqIntervallo[2] += 1

for i in range(3):
    prob[i] = iFreqIntervallo[i]/iNumProve
    print(f"la probabilità di trovare la variabile x_media entro {i+1} sigma è di: {round(prob[i]*100,2)}%")    

end = time.time()
print("Il tempo di esecuzione della procedura è: ", round(end-start,2))
    


