""" Calcolare la probabilità che lanciando due dadi:
a) la somma sia 5
b) escano due 1 """
import time
start = time.time()

import sys
sys.path.append("/home/studente26/IA 2/DIstribuzDiscrete")
from pkg_03052023.es01 import EstraiDaUrna


lUrna = [1]*6
iNumProve = 10**6
lFrequenze = [0,0]
lListaEventi = ["A","B"]

for i in range(iNumProve):
    iNum1 = EstraiDaUrna(lUrna) + 1 #+1 perchè estraggo l'indice che va da 0-5
    iNum2 = EstraiDaUrna(lUrna) + 1

    if iNum1 + iNum2 == 5:
        lFrequenze[0] += 1
    if iNum1 == 1 and iNum2  == 1:
        lFrequenze[1] += 1

for i in range(len(lListaEventi)):
    print(f"la probabilità dell'evento {lListaEventi[i]} è {round(lFrequenze[i]/iNumProve,3)}")

end = time.time()

print("Il tempo di esecuzione della procedura è: ", round(end-start,4))