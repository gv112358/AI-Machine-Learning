"""
lUrna1 = [4,4,4,4,4,4,4,4,4,4]
lUrna2 = [4,4,4,4,4,4,4,4,4,4,4,4,4]
"""

lUrna1 = [20,20]
lUrna2 = [28,24]


lSample = [2,3]

iNumProve = 1000000
iNumSuccessi1 = 0
iNumSuccessi2 = 0
lAppo = [0,0]
for i in range(iNumProve):
    lAppo = [0, 0]
    for j in range(5):
        num = EstraiDaUrna(lUrna1)
        if((num + 1)%2)==0:
            lAppo[0]+=1
        else:
            lAppo[1]+=1
    if lAppo == lSample:
        iNumSuccessi1+=1

for i in range(iNumProve):
    lAppo = [0, 0]
    for j in range(5):
        num = EstraiDaUrna(lUrna2)
        if((num+1)%2==0):
            lAppo[0]+=1
        else:
            lAppo[1]+=1
    if lAppo == lSample:
        iNumSuccessi2+=1


UrnaScelta = [iNumSuccessi1,iNumSuccessi2].index(max([iNumSuccessi1,iNumSuccessi2]))

print("L'urna scelta è ", UrnaScelta + 1)

lProb = [0, 0]
lProb[0] = iNumSuccessi1/(iNumSuccessi1 + iNumSuccessi2)
lProb[1] = iNumSuccessi2/(iNumSuccessi1 + iNumSuccessi2)
entropia = scipy.stats.entropy(lProb)
max_entropia = math.log(len(lProb))
entropia_relativa = entropia/max_entropia
print("Entropia: " + str(entropia) + " relativa: " + str(entropia_relativa))
sys.exit()