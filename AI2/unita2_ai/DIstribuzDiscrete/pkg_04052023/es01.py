import sys
sys.path.append("/home/studente26/IA 2/DIstribuzDiscrete")
from pkg_03052023.es01 import EstraiDaUrna
#sys.path.append('../')

#ripasso

lMiaUrna = [3,5,18]
lListaLabels = ["palline rosse", "palline gialle", "palline nere"]

for i in range(3):
    iEstrazione = EstraiDaUrna(lMiaUrna)
    print(f"L'estrazione {i+1} ha dato risultato: {lListaLabels[iEstrazione]}")

