"""Si stima che il 30% degli adulti negli Stati Uniti siano obesi, che il 3% siano
diabetici e che il 2% siano sia obesi che diabetici. Determina la probabilit`a
che un individuo scelto casualmente
1. sia diabetico se `e obeso;
2. sia obeso se `e diabetico"""
import time
start = time.time()


import sys
#sys.path.append("/home/studente26/IA 2/DIstribuzDiscrete")
sys.path.append("C:\\Users\giov\\Desktop\\Code\\IA 2\\DIstribuzDiscrete")
from pkg_03052023.es01 import EstraiDaUrna

iNumProveTot = 10**6
lNumProve = [0,0]
lFrequenze = [0,0]
lEventi = ["A", "B"]
lUrna = [2,28,1,69] #[O-D,O-ND,NO-D,NO-ND]

for i in range(iNumProveTot):
    iNum = EstraiDaUrna(lUrna)[0] 
    if iNum == 0 or iNum == 1: #Estraggo un Obeso
        lNumProve[0] += 1
        if iNum == 0: #conto i diabetici
            lFrequenze[0] += 1   
    if iNum ==0 or iNum == 2: #Estraggo un Diabetico
        lNumProve[1] += 1 
        if iNum == 0:
            lFrequenze[1] += 1

for i in range(len(lEventi)):
    print(f"La probabilità della richiesta {lEventi[i]} è: ", round(lFrequenze[i]/lNumProve[i],3))

end = time.time()
print("Il tempo di esecuzione della procedura è: ", round(end-start,2))



