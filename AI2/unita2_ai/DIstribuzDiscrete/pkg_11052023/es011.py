import time
start = time.time()

from random import randint


def PorceduraEstraiUrna(lurna):

    somaPallineLista = sum(lurna) 

    numCasuale = randint(1, somaPallineLista)

    lunghezzaLista = len(lurna) 

    ipartialLen = 0

    for i in range(lunghezzaLista):

        ipartialLen += lurna[i]

        if numCasuale <= ipartialLen:

            return i



lMiaUrna = [69,1,28,2]
# 00 - 01 - 10 - 11
numProve = 10000000


num = 0
num1 = 0

numObesi = 0
numDiabete = 0


for i in range(0,numProve):

    iEstrazione = PorceduraEstraiUrna(lMiaUrna)

    if iEstrazione == 2 or iEstrazione == 3:
            numObesi += 1

            if iEstrazione == 3 :
                 num += 1

    if iEstrazione == 1 or iEstrazione == 3:
            
            numDiabete += 1

            if iEstrazione == 3 :
                 num1 += 1

prob1 = num/numObesi
prob2 = num1/numDiabete



print("la probabilita che un obeso sia anche diabetico è di: " + str(prob1))
print("la probabilita che un diabetico sia anche obeso è di: " + str(prob2))

end = time.time()
print("Il tempo di esecuzione della procedura è: ", round(end-start,2))

import matplotlib.pyplot as plt

x = ["Popolazione sana", "Diabetici", "Obesi", "Diabetici Obesi", "Prob D, dato O", "Porb D, dato O"]
y = [0.69, 0.01, 0.28, 0.02,prob1, prob2]

plt.bar(x,y)
plt.show()