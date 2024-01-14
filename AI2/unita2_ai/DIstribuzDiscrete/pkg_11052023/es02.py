"""A un esame universitario si presentano sia studenti che hanno seguito il
corso sia studenti che non l’hanno seguito. Il docente ritiene che il 65% degli
studenti abbiano seguito il corso. La probabilit`a che uno studente superi
l’esame dato che ha seguito il corso `e 0.75, mentre la probabilit`a che uno
studente superi l’esame dato che non ha seguito il corso `e 0.40.
1
• Qual `e la probabilit`a che uno studente superi l’esame?
• Qual `e la probabilit`a che uno studente abbia seguito il corso dato che
ha superato l’esame?"""
import time
start = time.time()

import sys
#sys.path.append("/home/studente26/IA 2/DIstribuzDiscrete")
sys.path.append("C:\\Users\giov\\Desktop\\Code\\IA 2\\DIstribuzDiscrete")
from pkg_03052023.es01 import EstraiDaUrna

iNumProveTot = 10**6
lNumProve = [iNumProveTot,0]
lFrequenze = [0,0]
lEventi = ["A", "B"]
lUrna = [49,16,14,21] # seg-sup, seg-nsup, nseg-sup, nseg-nsup
# lProbEsame = [0.75, 0.40] 

for i in range(iNumProveTot):
    iNum = EstraiDaUrna(lUrna)[0]
    if iNum == 0 or iNum == 2:
        lFrequenze[0] += 1
        lNumProve[1] += 1
        if iNum == 0:
            lFrequenze[1] += 1

for i in range(len(lEventi)):
    print(f"La probabilità della richiesta {lEventi[i]} è: ", round(lFrequenze[i]/lNumProve[i],3))

end = time.time()
print("Il tempo di esecuzione della procedura è: ", round(end-start,2))