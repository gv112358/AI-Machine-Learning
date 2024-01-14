mu = 10
sigma = 4.5
alpha = 0.1

#genero un campione di 100 elementi (una lista di 100 elementi)
lUrna = [12,30,50,27,10]
lEtichette = [6,8,10,12,14]
media_campionaria = 0
for i in range(100):
    ret = EstraiDaUrna(lUrna)
    media_campionaria += lEtichette[ret]

#calcola la media sui 100 elementi
media_campionaria = media_campionaria/100

#richiama CalcolaCodaNormale
ret = CalcolaCodaNormale(mu,sigma/math.sqrt(100),media_campionaria)
if ret < alpha/2:
    print("L'ipotesi è rifiutata, cioè il campione non proviene dalla normale")
else:
    print("L'ipotesi è accettata")