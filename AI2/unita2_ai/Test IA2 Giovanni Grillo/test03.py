"""In un'urna ci sono 12 palline blu e 15 bianche. Estraggo una pallina: se è
blu estraggo l'altezza di una persona da una popolazione normale
con media 175 e scarto quadratico medio 6.5. Se esce una pallina 
bianca estraggo da una normale con media 195 e varianza 36. Qual'è la probabilità
di estrarre una persona più alta di 2 metri?"""

from random import randint
from numpy import random

def EstraiDaUrna(lUrna):
    somma = sum(lUrna)
    numEstratto = randint(1, somma)
    for i in range(len(lUrna)):
        if numEstratto <= sum(lUrna[:i+1]):
                return i

def EstraiDaNormale(fMu, fSigma):
    fRet = random.normal(fMu,fSigma,1)
    return fRet



#labels = [blu, bianche]
lUrna =[12,15]

fMu1 = 175
fSigma1 = 6.5

fMu2 =195
fSigma2 = 6

iNumProve = 1000000
iEstrazione = 0
fRet = 0
freq = 0

for i in range(iNumProve):
     iEstrazione = EstraiDaUrna(lUrna)
     if iEstrazione == 0:
          fRet = EstraiDaNormale(fMu1,fSigma1)
          if fRet > 200:
               freq += 1
     if iEstrazione == 1:
          fRet = EstraiDaNormale(fMu2,fSigma2)
          if fRet > 200:
               freq += 1

print(f"La probabilità richiesta è di: {round(freq/iNumProve,3)}")