"""Dato un campione di 100 elementi, verifica quanto è probabile
che sia stato estratto da una normale N(10,4.5)
1) se l'ipotesi è vera, allora media_campione si distribuisce N(10,0.45). Per verificare l'ipotesi posso calcolare l'area delle code
più è piccola e meno è probabile che l'ipotesi sia vera, perchè il dato si distribuesce all'esterno"""
import time
start = time.time()

import sys
sys.path.append("/home/studente26/IA 3")
#sys.path.append("C:\\Users\giov\\Desktop\\Code\\IA 3")
from Procedure.Estrazioni import ExNormale, ExUrna,CalcolaCodaNormale
from math import sqrt

fMu = 10
fSigma = 0.45
alpha = 0.1 # soglia di accettabilità per il Z-Test
iCampione = 100
x= [0]*iCampione
lUrna = [12,31,55,28,7] #frequenze di un'urna tipo normale
lPedine = [6,8,10,12,14] #simulo un campione la cui media è 10

for i in range(iCampione):
    x[i] = lPedine[ExUrna(lUrna)]
media_campionaria = sum(x)/iCampione
print(f"la media campionaria è {media_campionaria}")

coda = CalcolaCodaNormale(fMu, fSigma, media_campionaria)
print(f"la coda rispetto a N(10,0.45) è : {round(coda,3)}")

if coda < alpha/2:
    print("l'ipotesi è rifiutata, il campione non proviene da N(10,4.5)")
else:
    print("L'ipotesi è accettata")
end = time.time()
print(f"Il tempo di esecuzione della procedura è: {round(end-start,2)} sec "  )




