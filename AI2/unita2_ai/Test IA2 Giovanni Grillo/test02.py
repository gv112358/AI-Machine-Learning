"""Nel 1970 i Beatles vennero a Genova in incognito e pernottarono 
all’albergo Nicolas Bourbaki (ora distrutto per costruire 
l’attuale dipartimento di matematica). L’albergo aveva 10 camere 
di lusso disposte ai due lati di un corridoio rettilineo 
dell’ultimo piano, 5 per lato. A ciascuno dei cantanti venne assegnata 
a caso una camera: 
qual è la probabilità che, almeno due di loro, 
avessero camere contigue ?"""

from random import randint

def EstraiDaUrna(lUrna):
    somma = sum(lUrna)
    numEstratto = randint(1, somma)
    for i in range(len(lUrna)):
        if numEstratto <= sum(lUrna[:i+1]):
                return i

lMiaUrna = [1]*10 #genero 10 camere distinte
iNumProve = 1_000_000
freq = 0
freqPrecedente = 0
iEstrazione = 0


for j in range(iNumProve):
        camereLato1 = []
        camereLato2 = []
        camereTotali = []

        #assegno le camere casualmente
        while len(camereTotali)<4:
              iEstrazione = EstraiDaUrna(lMiaUrna)
              if iEstrazione <=4 : #separo le camere in due liste
                if iEstrazione not in camereLato1:  #controllo che la stessa camera non venga riassegnata
                    camereLato1.append(iEstrazione)
                    camereTotali.append(iEstrazione)
              else:
                if iEstrazione not in camereLato2: 
                    camereLato2.append(iEstrazione)
                    camereTotali.append(iEstrazione)
        
        camereL1Ordinate = sorted(camereLato1) 
        camereL2Ordinate = sorted(camereLato2)

        if len(camereL1Ordinate) >1: #controllo se ci sono camere assegnate dal lato 1 
            for i in range(len(camereL1Ordinate) - 1):
                if camereL1Ordinate[i] + 1 == camereL1Ordinate[i+1]:
                    freq += 1
                    break #interrompo per non contarne altri, ne bastano 2 
        
        if freq == freqPrecedente and len(camereL2Ordinate) >1: #controllo di non aver già trovato due camere contigue dal lato 1

            for i in range(len(camereL2Ordinate) - 1):
                if camereL2Ordinate[i] + 1 == camereL2Ordinate[i+1]:
                    freq += 1
                    break

        freqPrecedente = freq 
            
print(f"la probabilità richiesta è: {round(freq/iNumProve,3)}")
      

                