import time
start = time.time()

import sys
sys.path.append("/home/studente26/IA 2/DIstribuzDiscrete")
#sys.path.append("C:\\Users\giov\\Desktop\\Code\\IA 2\\DIstribuzDiscrete")
from Procedure.Estrazioni import ExUrna
from Procedure.grafici import CreaGrafoCartesiano as cgc



#iNumPersone = 23
lUrna = [1]*365
iNumProve = 10**4
iNumSuccessi = 0
probabilita = 0

lX = []
lY = []
for iNumPersone in range(2,30):
    iNumSuccessi = 0

    for i in range(iNumProve):
        ldate = []
        for j in range(iNumPersone):
            idataEstratta = ExUrna(lUrna)
            if idataEstratta in ldate:
                iNumSuccessi += 1
                break
            else:
                ldate.append(idataEstratta)      
            
    probabilita = iNumSuccessi/iNumProve
    lX.append(iNumPersone)
    lY.append(probabilita)
    print("Prova per " + str(iNumPersone) + " persone -> probabilità: " + str(probabilita))

#print(f"la probabilità di avere 2 persone nate lo stesso giorno è: ", probabilita)
print(lX)
print(lY)

cgc("Paradosso dei Compleanni", ["Numero persone","Probabilità"],"purple",lX,lY)

end = time.time()
print("Il tempo di esecuzione della procedura è: ", round(end-start,2))