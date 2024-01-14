from random import randint
import sys
#scrivere una procedura Estrai da Urna che prende in input la lista che rappresenta l'urna
#conta le palline dell'urna (come elementi della lista)
#genera un intero da 1 al numero di elementi totale
#ciclo for ad 1 a SommaElementiLista
    #ciclo for interno per la dimensione della lista
    #   if con individuazione della classe 

"""for i in range(0,10):
    numCasuale = randint(1,6)
    print(numCasuale)"""

def istogramma(x):
    d = dict()
    if x not in d:
        d[x] = 1
    else:
        d[x] +=1
    return d

def EstraiDaUrna(lUrna, mod0ConInserimento1Senza=0):
    somma = sum(lUrna)
    numEstratto = randint(1, somma)
    # print("Il numero estrotto è: ", numEstratto)
    for i in range(len(lUrna)):
        if numEstratto <= sum(lUrna[:i+1]):
    #        print("il numero estratto è associato alla posizione: ", i)
            if mod0ConInserimento1Senza == 0:
                return i, lUrna
            else:
                lUrna[numEstratto] -= 1
                return i, lUrna

def ExUrna(lUrna):
    somma = sum(lUrna)
    numEstratto = randint(1, somma)
    for i in range(len(lUrna)):
        if numEstratto <= sum(lUrna[:i+1]):
                return i

"""
lMiaUrna = [10,5,3] 
iRet = EstraiDaUrna(lMiaUrna) #l'indice della lista è associato al colore estratto
"""
    