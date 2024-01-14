"""1) Si considerino due urne: la prima contenente 2 palline rosse e 8 verdi e la seconda contenente 4 palline rosse e 6 verdi.
a) Si consideri un esperimento che consiste nell’estrarre con ripetizione
due palline dalla prima urna e si determini la probabilità che entrambe le palline siano rosse.
b) Si consideri l’esperimento che consiste nell’estrarre una pallina dalla
prima urna, nell’inserirla nella seconda urna e nell’estrarre una pallina dalla seconda urna. Determinare la probabilità che la pallina estratta sia rossa.
c) Sapendo che la pallina estratta dalla seconda urna è rossa, calcolare la probabilità che la pallina estratta dalla prima urna sia verde."""
import time
start = time.time()

import sys
#sys.path.append("/home/studente26/IA 2/DIstribuzDiscrete")
sys.path.append("C:\\Users\giov\\Desktop\\Code\\IA 2\\DIstribuzDiscrete")
from pkg_03052023.es01 import EstraiDaUrna

def CondizioneA(iEstrazione1, iEstrazione2):
    if iEstrazione1 == 0 and iEstrazione2 == 0:
        return 1
    return 0

def CondizioneB(iEstrazione1,iEstrazione2):
    if iEstrazione2 == 0:
        return 1
    return 0

lUrna1 = [2,8]
lUrna2 = [4,6]
lNumProve = [10**6,10**6,0]
lListaEventi = ["A", "B", "C"]
lFrequenze = [0,0,0]

# Evento A
for i in range(lNumProve[0]):
    iNum1 = EstraiDaUrna(lUrna1)[0]
    iNum2 = EstraiDaUrna(lUrna1)[0]

    if CondizioneA(iNum1, iNum2):
        lFrequenze[0] += 1
# Evento B
for i in range(lNumProve[0]):
    iNum1 = EstraiDaUrna(lUrna1)[0]
    lUrna2[iNum1] += 1
    iNum2 = EstraiDaUrna(lUrna2)[0]

    if iNum2 == 0: 
        lNumProve[2] += 1 # conto per l'evento C
        if i>0 and iNum1 == 1:
            lFrequenze[2] +=1

    if CondizioneB(iNum1, iNum2) == 1: # Evento B
        lFrequenze[1] += 1    
    #iNum1 = EstraiDaUrna(lUrna1)

    lUrna2 = [4,6] #ripristino urna 2

for i in range(len(lListaEventi)):
    print(f"la probabilità dell'evento {lListaEventi[i]} è {round(lFrequenze[i]/lNumProve[i],3)}")

end = time.time()

print("Il tempo di esecuzione della procedura è: ", round(end-start,2))







