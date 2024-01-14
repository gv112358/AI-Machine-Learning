"""Data una popolazione normale di media 12 e varianza 16 indicare approssimativamente quel 
valore della X che lascia alla sua destra il 13% dei casi."""

from numpy import random
def EstraiDaNormale(fMu, fSigma):
    fRet = random.normal(fMu,fSigma,1)
    return fRet

fMu = 12
fSigma = 4
iNumProve = 10**6
iSuccessi = 0
lSuccessi = [0]*5

# entro 12 resta fuori il 50%
# entro 12+4 = 16 resta fuori 15.85%
# provo da 16.3 in poi 
for i in range(iNumProve):
    fRet = EstraiDaNormale(fMu,fSigma)
    if fRet >= 16.3:
        lSuccessi[0] += 1
    if fRet >= 16.4:
        lSuccessi[1] += 1
    if fRet >= 16.5:
        lSuccessi[2] += 1
    if fRet >= 16.6:
        lSuccessi[3] += 1
    if fRet >= 16.7:
        lSuccessi[4] += 1

lProb = [ x*100/iNumProve for x in lSuccessi]
lTest = [16.3, 16.4, 16.5,16.6,16.7]

for i in range(len(lProb)):
    print(f" Rispetto a x = {lTest[i]} si ottiene il {round(lProb[i],2)} del campione")

print("Il valore cercato della variabile x è circa 16.5")
