from numpy import random
from random import randint

def ExNormale(fMu, fSigma):
    fRet = random.normal(fMu,fSigma,1)
    return fRet

""" Si può anche realizzare con randint e la procedura Exurna, dove le palline nere sono stanno sotto la gaussiana e bianche sopra
prendendo 1000 palline, se estratto<gaussiana(x) allora sucecssi ok"""

def ExUrna(lUrna):
    somma = sum(lUrna)
    numEstratto = randint(1, somma)
    for i in range(len(lUrna)):
        if numEstratto <= sum(lUrna[:i+1]):
                return i

#EstraiDaNormale (media,sigma,numerosità campionaria)
def ExMCN(fMu,fSigma,c):
    media = 0
    for i in range(c):
        ret = ExNormale(fMu, fSigma)
        media += ret
    return media/c

def CalcolaCodaNormale(fMu,fSigma,fXvalue):
    iNumProve = 10**6
    iCoda = 0
    if fXvalue < fMu:
        for i in range(iNumProve):
            ret = ExNormale(fMu, fSigma)
            if ret < fXvalue:
                iCoda += 1
    elif fXvalue > fMu:
        for i in range(iNumProve):
            ret = ExNormale(fMu, fSigma)
            if ret > fXvalue:
                iCoda += 1
    return iCoda/iNumProve

def ExUniforme(fStart,fEnd):
    return random.uniform(fStart,fEnd,1)

def ExPoisson(iLambda):
    return random.poisson(iLambda,1)

def ExChiQuadro(iK):
    return random.chisquare(iK,1)