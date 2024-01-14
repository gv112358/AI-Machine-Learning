import numpy
import pandas as pd
import sys
sys.path.append("/home/studente26/IA 3")
#sys.path.append("C:\\Users\giov\\Desktop\\Code\\IA 3")
from Procedure.Estrazioni import ExNormale, ExUniforme, ExPoisson, ExChiQuadro
import matplotlib.pyplot as plt


c = 20 #numerosità campionaria 
iNumProve = 1000 

#Parametri Normale:
Mu = 20
sigma = 2
#Parametri Uniforme
a = 5
b = 15
#Parametri Poisson
lamb = 2
#Parametri Chi Quadro
k = 5


def GeneraDist(c,iNumProve,Distribuzione):
    x=[0]*c #lista estratti
    medie= [0]*iNumProve #lista medie
    for j in range(iNumProve):
        for i in range(c):
            x[i] = Distribuzione(a,b)
        df = pd.DataFrame(x)
        medie[j] = df[0].mean()

    df = pd.DataFrame(medie)
    skew = df[0].skew()
    curtosi = df[0].kurt()
    print(f"la skewness vale: ", round(skew,3))
    print(f"la curtosi vale: ", round(curtosi,3))
    df.plot.hist()
    plt.show()

GeneraDist(c,iNumProve,ExUniforme(a,b))
GeneraDist(c,iNumProve,ExNormale)
GeneraDist(c,iNumProve,ExPoisson)
GeneraDist(c,iNumProve,ExChiQuadro)




