"""
Data una popolazione di 100 maschi e 128 femmine, tenendo presente che 1/3 dei maschi
hanno scelto il liceo mentre il restante hanno scelto il tecnico,
e tenendo presente che la metà delle femmine ha scelto il liceo e le restanti il tecnico,

calcolare la probabilità di incontrare una persona che ha scelto il tecnico oppure una donna?

lUrna = [m_t,m_l,f_t,f_l]
lUrna = [67, 33, 64, 64]
lEventi = [1,0,1,1]

"""
from es03 import CalcolaProbabilita

iNumProve = 1000000
#Urna = [m_t,m_l,f_t,f_l]
lUrna = [67, 33, 64, 64]
lEventi = [1,0,1,1]

print(CalcolaProbabilita(iNumProve, lUrna, lEventi))



