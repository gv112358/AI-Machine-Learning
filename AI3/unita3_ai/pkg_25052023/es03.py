lUrna1 = [20,32,12]
lUrna2 = [32,32,32]
lUrna3 = [20,20,21]
lSample = [6,8,5]

iNumProve = 1000000
iNumSuccessi1 = 0
iNumSuccessi2 = 0
iNumSuccessi3 = 0
lAppo = [0,0,0]
for i in range(iNumProve):
    lAppo = [0, 0, 0]
    for j in range(19):
        num = EstraiDaUrna(lUrna1)
        lAppo[num]+=1
    if lAppo == lSample:
        iNumSuccessi1+=1

for i in range(iNumProve):
    lAppo = [0, 0, 0]
    for j in range(19):
        num = EstraiDaUrna(lUrna2)
        lAppo[num]+=1
    if lAppo == lSample:
        iNumSuccessi2+=1

for i in range(iNumProve):
    lAppo = [0, 0, 0]
    for j in range(19):
        num = EstraiDaUrna(lUrna3)
        lAppo[num]+=1
    if lAppo == lSample:
        iNumSuccessi3+=1
UrnaScelta = max([iNumSuccessi1,iNumSuccessi2,iNumSuccessi3])
print("L'urna scelta è ", UrnaScelta)

lProb = [0.2, 0.7, 0.1]
entropia = scipy.stats.entropy(lProb)
max_entropia = math.log(len(lProb))
entropia_relativa = entropia/max_entropia
print("Entropia: " + str(entropia) + " relativa: " + str(entropia_relativa))
sys.exit()