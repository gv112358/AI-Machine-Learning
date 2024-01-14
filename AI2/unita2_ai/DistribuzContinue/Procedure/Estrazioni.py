from numpy import random

def ExNormale(fMu, fSigma):
    fRet = random.normal(fMu,fSigma,1)
    return fRet

""" Si può anche realizzare con randint e la procedura Exurna, dove le palline nere sono stanno sotto la gaussiana e bianche sopra
prendendo 1000 palline, se estratto<gaussiana(x) allora sucecssi ok"""
