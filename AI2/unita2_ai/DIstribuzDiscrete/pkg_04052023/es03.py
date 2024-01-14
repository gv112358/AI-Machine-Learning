#funzione che prende 3 argomenti, iNumProve, lUrna e lEventi
# lUrna = [10,7,32,31,31]
#lLabels = ["pere", "carote", "mele", "zucchine", "pesche"]
# probabilità di estrarre un frutto : lEventi=[1,0,1,0,1]
import sys
sys.path.append("/home/studente26/IA 2/DIstribuzDiscrete")
from pkg_03052023.es01 import EstraiDaUrna


def CalcolaProbabilita(iNumProve,lUrna,lEventi):
    lListaFrequenze = [0]*len(lEventi)
    probabilita = 0
    if str(iNumProve).isnumeric() and (type(lUrna) and type(lEventi) is list) and (len(lUrna) == len(lEventi)):

        for i in range(iNumProve):
            iEstrazione = EstraiDaUrna(lUrna)
            if lEventi[iEstrazione] == 1: 
                lListaFrequenze[iEstrazione]+=1
        
        probabilita = sum(lListaFrequenze)/iNumProve
        return round(probabilita,3)    
    else:
        
        print("Parametri non inseriti correttamente")
        pass


"""iNumProve = 1000000
lUrna = [10,7,32,31,31]
lEventi=[1,0,1,0,1]
print(CalcolaProbabilita(iNumProve, lUrna, lEventi))"""

