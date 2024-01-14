import numpy
import pandas as pd
import sys
sys.path.append("/home/studente26/IA 3")
#sys.path.append("C:\\Users\giov\\Desktop\\Code\\IA 3")
from Procedure.Estrazioni import ExNormale, ExUniforme, ExPoisson, ExChiQuadro
import matplotlib.pyplot as plt
from math import sqrt


c = 20 #numerosità campionaria 
iNumProve = 1000

#Parametri Normale:
Mu = 20
sigma = 2
sigmaNormNew = sigma/sqrt(c)
#Parametri Uniforme
a = 5
b = 15
MuUni = (a+b)/2
sigmaUni= ((b-a))/sqrt(12)
sigmaUniNew = sigmaUni/sqrt(c)
#Parametri Poisson
lamb = 2
sigmaPois= sqrt(lamb)
sigmaPoisNew = lamb/sqrt(c)
#Parametri Chi Quadro
k = 5
sigmaCQ= sqrt(2*k)
sigmaCQNew = sigmaCQ/sqrt(c)



# Distribuzione Uniforme
print(f"************DISTRIBUZIONE UNIFORME*********")
x=[0]*c #lista estratti
medie= [0]*iNumProve #lista medie
iFreqIntervallo = [0]*3
prob = [0]*3
fMu_media=MuUni
fSigma_media = sigmaUniNew
for j in range(iNumProve):
    for i in range(c):
        x[i] = ExUniforme(a,b)
    df1 = pd.DataFrame(x)
    medie[j] = df1[0].mean()
    x_media = medie[j]
    if x_media >= (fMu_media - fSigma_media) and x_media <= (fMu_media + fSigma_media):
            iFreqIntervallo[0] += 1
    if x_media >= (fMu_media - fSigma_media*2) and x_media <= (fMu_media + fSigma_media*2):
            iFreqIntervallo[1] += 1
    if x_media >= (fMu_media - fSigma_media*3) and x_media <= (fMu_media + fSigma_media*3):
            iFreqIntervallo[2] += 1
for i in range(3):
    prob[i] = iFreqIntervallo[i]/iNumProve
    print(f"la probabilità di trovare la variabile x_media entro {i+1} sigma è di: {round(prob[i]*100,2)}%")
df1 = pd.DataFrame(medie)
skew = df1[0].skew()
curtosi = df1[0].kurt()
print(f"la skewness vale: ", round(skew,3))
print(f"la curtosi vale: ", round(curtosi,3))
df1.plot.hist()
plt.show()



# Distribuzione Normale
print(f"************DISTRIBUZIONE NORMALE *********")
x=[0]*c #lista estratti
medie= [0]*iNumProve #lista medie
iFreqIntervallo = [0]*3
prob = [0]*3
fMu_media=Mu
fSigma_media = sigmaNormNew
for j in range(iNumProve):
    for i in range(c):
        x[i] = ExNormale(Mu,sigma)
    df2 = pd.DataFrame(x)
    medie[j] = df2[0].mean()
    x_media=medie[j]
    if x_media >= (fMu_media - fSigma_media) and x_media <= (fMu_media + fSigma_media):
            iFreqIntervallo[0] += 1
    if x_media >= (fMu_media - fSigma_media*2) and x_media <= (fMu_media + fSigma_media*2):
            iFreqIntervallo[1] += 1
    if x_media >= (fMu_media - fSigma_media*3) and x_media <= (fMu_media + fSigma_media*3):
            iFreqIntervallo[2] += 1
for i in range(3):
    prob[i] = iFreqIntervallo[i]/iNumProve
    print(f"la probabilità di trovare la variabile x_media entro {i+1} sigma è di: {round(prob[i]*100,2)}%")
df2 = pd.DataFrame(medie)
skew = df2[0].skew()
curtosi = df2[0].kurt()
print(f"la skewness vale: ", round(skew,3))
print(f"la curtosi vale: ", round(curtosi,3))
df2.plot.hist()
plt.show()



# Distribuzione Poisson
print(f"************DISTRIBUZIONE POISSON *********")
x=[0]*c #lista estratti
medie= [0]*iNumProve #lista medie
iFreqIntervallo = [0]*3
prob = [0]*3
fMu_media=lamb
fSigma_media = sigmaPoisNew
for j in range(iNumProve):
    for i in range(c):
        x[i] = ExPoisson(lamb)
    df3 = pd.DataFrame(x)
    medie[j] = df3[0].mean()
    x_media=medie[j]
    if x_media >= (fMu_media - fSigma_media) and x_media <= (fMu_media + fSigma_media):
            iFreqIntervallo[0] += 1
    if x_media >= (fMu_media - fSigma_media*2) and x_media <= (fMu_media + fSigma_media*2):
            iFreqIntervallo[1] += 1
    if x_media >= (fMu_media - fSigma_media*3) and x_media <= (fMu_media + fSigma_media*3):
            iFreqIntervallo[2] += 1
for i in range(3):
    prob[i] = iFreqIntervallo[i]/iNumProve
    print(f"la probabilità di trovare la variabile x_media entro {i+1} sigma è di: {round(prob[i]*100,2)}%")

df3 = pd.DataFrame(medie)
skew = df3[0].skew()
curtosi = df3[0].kurt()
print(f"la skewness vale: ", round(skew,3))
print(f"la curtosi vale: ", round(curtosi,3))
df3.plot.hist()
plt.show()

# Distribuzione Chi Quadro
print(f"************DISTRIBUZIONE CHI QUADRO *********")
x=[0]*c #lista estratti
medie= [0]*iNumProve #lista medie
iFreqIntervallo = [0]*3
prob = [0]*3
fMu_media=k
fSigma_media = sigmaCQNew
for j in range(iNumProve):
    for i in range(c):
        x[i] = ExChiQuadro(k)
    df4 = pd.DataFrame(x)
    medie[j] = df4[0].mean()
    x_media=medie[j]
    if x_media >= (fMu_media - fSigma_media) and x_media <= (fMu_media + fSigma_media):
            iFreqIntervallo[0] += 1
    if x_media >= (fMu_media - fSigma_media*2) and x_media <= (fMu_media + fSigma_media*2):
            iFreqIntervallo[1] += 1
    if x_media >= (fMu_media - fSigma_media*3) and x_media <= (fMu_media + fSigma_media*3):
            iFreqIntervallo[2] += 1
for i in range(3):
    prob[i] = iFreqIntervallo[i]/iNumProve
    print(f"la probabilità di trovare la variabile x_media entro {i+1} sigma è di: {round(prob[i]*100,2)}%")

df4 = pd.DataFrame(medie)
skew = df4[0].skew()
curtosi = df4[0].kurt()
print(f"la skewness vale: ", round(skew,3))
print(f"la curtosi vale: ", round(curtosi,3))
df4.plot.hist()
plt.show()
