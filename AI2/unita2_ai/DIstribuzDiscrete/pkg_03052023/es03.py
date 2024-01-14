from es01 import EstraiDaUrna
"""
In un’urna ci sono 3 palline bianche e 
2 nere. Calcolare la probabilità che in due estrazioni 
(reintroducendo la pallina estratta, prima di estrarre la seconda pallina ): 

A - escano due palline nere  * 
B - escano due palline bianche + 
C - due palline di diverso colore -
"""

lMiaUrna = [3,2] #3 bianche, 2 nere
lListaEventi = ["A","B","C"]
lListaProbabilita = [0,0,0]
lListaFrequenze = [0,0,0] # richieste A, B, C
iNumProve = 1000000
for i in range(iNumProve):
    iNum1 = EstraiDaUrna(lMiaUrna)
    iNum2 = EstraiDaUrna(lMiaUrna)
    if iNum1 == 1 and iNum2 == 1:
        lListaFrequenze[0] += 1
    if iNum1 == 0 and iNum2 == 0:
        lListaFrequenze[1] +=1
    if iNum1 != iNum2:
        lListaFrequenze[2] +=1

for i in range(3):
    lListaProbabilita[i]=lListaFrequenze[i]/iNumProve

probTot = sum((lListaProbabilita))

for i in range(len(lListaEventi)):
    print(f"la probabilità dell'evento {lListaEventi[i]} è {round(lListaProbabilita[i],4)}")
print(("La probabilità totale degli eventi è: ", probTot))

    
