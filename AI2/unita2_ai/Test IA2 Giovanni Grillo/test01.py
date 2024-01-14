"""Un'urna è composta da 12 palline rosse, 20 palline bianche,
40 palline azzurre e 38 palline gialle. In 4 estrazioni,
rimettendo ogni volta la pallina estratta, calcolare:

A: la probabilità di estrarre 2 palline gialle e 2 azzurre
B: la probabilità di estrarre almeno 3 palline gialle
C: la probabilità che, dato che almeno una pallina è gialla,ve ne siano almeno 2 di colore uguale"""

from random import randint

def EstraiDaUrna(lUrna):
    somma = sum(lUrna)
    numEstratto = randint(1, somma)
    for i in range(len(lUrna)):
        if numEstratto <= sum(lUrna[:i+1]):
                return i

#labels = [ rosse, bianche, azzurre, gialle]
lMiaUrna = [12,20,40,38]
iNumProve = 10**6
iNumProve1 = 0
lFreq=[0]*3
lProve=[10**6,10**6,0]
lEventi=["A", "B", "C"]
lProb = [0]*3

#ripeto per 1 milione di volte
for i in range(iNumProve):

     iFrequenzaRosse = 0
     iFrequenzaBianche = 0
     iFrequenzaAzzurre = 0
     iFrequenzaGialle = 0

#simulo le 4 estrazioni
     for k in range(4):
          iEstrazione = EstraiDaUrna(lMiaUrna)
        
          if iEstrazione == 0:
            iFrequenzaRosse += 1
          if iEstrazione == 1:
            iFrequenzaBianche += 1
          if iEstrazione == 2:
            iFrequenzaAzzurre += 1
          if iEstrazione == 3:
            iFrequenzaGialle += 1
      
     if iFrequenzaGialle and iFrequenzaAzzurre == 2:
        lFreq[0] += 1; 
     if iFrequenzaGialle >= 3:
        lFreq[1] += 1;
     if iFrequenzaGialle >=1:
         lProve[2] += 1
         if iFrequenzaGialle >= 2 or iFrequenzaAzzurre >= 2 or iFrequenzaBianche >= 2 or iFrequenzaRosse >= 2:
        
             lFreq[2] += 1

#lProb = [x / y for x, y in zip(lFreqy, lProve)]

for i in range(len(lProb)):
    lProb[i] = lFreq[i]/lProve[i]
    print(f"La probabilità dell'evento {lEventi[i]} è: {round(lProb[i],3)}")




    
    

    



    
    



