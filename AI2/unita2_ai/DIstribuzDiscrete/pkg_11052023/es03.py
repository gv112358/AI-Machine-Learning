"""Determinare il numero delle persone in un gruppo tale che la probabilità che il compleanno di due ricada 
nello stesso giorno sia maggiore o uguale al 50%"""

import time
start = time.time()

import sys
sys.path.append("/home/studente26/IA 2/DIstribuzDiscrete")
#sys.path.append("C:\\Users\giov\\Desktop\\Code\\IA 2\\DIstribuzDiscrete")
from pkg_03052023.es01 import ExUrna

frequenza = 0
iProveTot = 10**4
lGiorni = [1]*365
iNumGruppo = 19
probabilita = 0

while probabilita < 0.5:
    iNumGruppo += 1
    frequenza = 0
    for i in range(iProveTot):
        lDate = [0]*iNumGruppo
        for i in range(iNumGruppo):
            lDate[i] = ExUrna(lGiorni)
        sDate = set(lDate)
        if len(sDate) != len(lDate):        
            frequenza += 1
    probabilita = frequenza/iProveTot

print(f"Per un numero di {iNumGruppo} persone si ha una probabilità del {round(probabilita*100,1)}% di fare il compleanno lo stesso giorno" )
end = time.time()
print("Il tempo di esecuzione della procedura è: ", round(end-start,2))



"""
lGiorniCompleanni = [0]*10 #parto da un gruppo di 10 persone
lMesiCompleanni = [0]*10
for i in range(len(lGiorniCompleanni)):
    lGiorniCompleanni[i] = randint(1,30)
for i in range(len(lMesiCompleanni)):
    lMesiCompleanni[i] = randint(1,12)

for i in range(iNumProveTot):
    iGiorno1 = ExUrna(lGiorniCompleanni)
    iMese1 = ExUrna(lMesiCompleanni)
    iGiorno2 = ExUrna(lGiorniCompleanni)
    iMese2 = ExUrna(lMesiCompleanni)
    
    if iGiorno1 == iGiorno2 and iMese1 == iMese2:
        frequenza += 1 
            
probabilita  = frequenza/iNumProveTot
  """  
     



    
