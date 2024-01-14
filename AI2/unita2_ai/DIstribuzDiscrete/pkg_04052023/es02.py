
import sys
#sys.path.append('../')
sys.path.append("/home/studente26/IA 2/DIstribuzDiscrete")
from pkg_03052023.es01 import EstraiDaUrna
#Procedura che estrae 3 palline da un'urna **senza reinserimento**

def GeneraNuovaUrna(lUrna,iEstrazione):
    lUrna[iEstrazione]-=1
    return lUrna

lMiaUrna = [3,5,18]
lListaLabels = ["pallina rossa", "pallina gialla", "pallina nera"]

for i in range(3):
    iEstrazione = EstraiDaUrna(lMiaUrna)
    lMiaUrna = GeneraNuovaUrna(lMiaUrna, iEstrazione)
    print(f"L'estrazione {i+1} ha dato risultato: {lListaLabels[iEstrazione]}")

