from es01 import EstraiDaUrna

#estraiamo una carta da un mazzo, specificando numero e seme

listaValori = [4]*10 #10 valori su 4 semi
listaSemi = [10]*4 #4 semi su 10 valori

semi = ['bastoni', 'coppe','denari', 'spade']

valore = EstraiDaUrna(listaValori)

seme = EstraiDaUrna(listaSemi)

print("La carta estratta è: " + str(valore+1) + " di " + semi[seme])

iNumProve = 10**6
lListaFrequenze = [0]*10
for i in range(iNumProve):
    iNumero = EstraiDaUrna(listaValori)
    lListaFrequenze[iNumero] += 1
print(lListaFrequenze)