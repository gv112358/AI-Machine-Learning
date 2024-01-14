""" 2) Di tutti gli ATM collocati in Toscana, il 45% non ha subito attacchi nel
periodo 2009-2011, il 75% non ha subito attacchi nel periodo 2012-2014,
il 35% non ha subito attacchi in nessuno dei due periodi. Si selezioni
casualmente un ATM.
Sia
A l'evento che si verifica se l'ATM selezionato non ha subito attacchi nel
periodo 2009-2011 e B l'evento che si verifica se l'ATM selezionato non ha
subito attacchi nel periodo 2012-2014.
a) Calcolare P(B).
b) Sapendo che un ATM non ha subito attacchi nel periodo 2012-2014,
calcolare la probabilità che l’ATM non abbia subito attacchi nel periodo
2009-2011 (ovvero calcolareP(A|B)) e specificare se i due eventi sono indipendenti.
c) Calcolare 𝑃(𝐴 ∪ 𝐵)."""


import time
start = time.time()

import sys
#sys.path.append("/home/studente26/IA 2/DIstribuzDiscrete")
sys.path.append("C:\\Users\giov\\Desktop\\Code\\IA 2\\DIstribuzDiscrete")
from pkg_03052023.es01 import EstraiDaUrna
"""
#lLabels1 = ["non attaccati", "attaccati"]
lUrna1 = [450,550]
#lLabels2 = ["non attaccati mai", "non attaccati 2012", "attaccati 2012"]
lUrna20 = [350,100] #non attacati mai, non attaccati ma poi attacacati
lUrna1 = [400,150] #attaccati ma poi non attaccati, attaccati sempre"""
lUrna2 = [750,250] # non attaccati, attaccati 2012-2014
lUrna1 = [350,650] # mai attaccati, attaccati almeno una volta tra 2009-2014

lNumProve = [10**6,0]
lFrequenze = [0,0]
lEventi = ["A", "B"]

for i in range(lNumProve[0]):
    iNum2 = EstraiDaUrna(lUrna2)[0]
    if iNum2 == 0:
        lFrequenze[0] += 1
        lNumProve[1] += 1
        iNum1 = EstraiDaUrna(lUrna1)[0]
        if iNum1 == 0:
            lFrequenze[1] += 1
    """if i>0 and 
    iNum21 = EstraiDaUrna(lUrna21)
    iNum1 = EstraiDaUrna(lUrna1)
    if iNum21 and iNum20 == 0:
        lNumProve[1] += 1
        if i>0 and iNum1 == 1:
            lFrequenze[1] +=1"""

for i in range(len(lEventi)):
    print(f"La probabilità della richiesta {lEventi[i]} è: ", round(lFrequenze[i]/lNumProve[i],3))

end = time.time()
print("Il tempo di esecuzione della procedura è: ", round(end-start,2))





