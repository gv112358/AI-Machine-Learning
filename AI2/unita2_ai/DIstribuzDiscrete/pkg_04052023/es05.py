"""Un'urna contiene 90 palline numerate da 1 a 90.
Si estraggono 2 palline.
Calcolare la probabilità di avere:
A) Due numeri dispari
B) Un numero divisibile per 5 e uno non divisibile per 5
C) Due numeri la cui somma è 50
Considera sia la situazione in cui le palline si estraggono contemporaneamente 
(senza reinserimento) sia quella in cui la pallina venga rimessa all'interno dell'urna (con reinserimento)"""

#definizione urna
import sys
sys.path.append("/home/studente26/IA 2/DIstribuzDiscrete")
from pkg_03052023.es01 import EstraiDaUrna

lUrna = [1]*90
iNumProve = 10**6
lFrequenze = [0,0,0]
lProbabilita = [0,0,0]
lListaEventi = ["A","B","C"]

for i in range(iNumProve):
    iNum1 = EstraiDaUrna(lUrna)[0] + 1 #+1 perchè estraggo l'indice che va da 0-89
    iNum2 = EstraiDaUrna(lUrna)[0] + 1

    if iNum1%2 != 0 and iNum2%2 != 0:
        lFrequenze[0] += 1
    if (iNum1%5 == 0 and iNum2%5 != 0) or (iNum1%5 != 0 and iNum2%5 == 0):
        lFrequenze[1] += 1
    if (iNum1 + iNum2) == 50:
        lFrequenze[2] += 1

for i in range(len(lListaEventi)):
    print(f"la probabilità dell'evento {lListaEventi[i]} è {round(lFrequenze[i]/iNumProve,2)}")






