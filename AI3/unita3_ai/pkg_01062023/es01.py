""" max {M1,...Mn} prob(x1,...,xk|Mi)
Voglio costruire un correttore ortografico. Parto da un dizionario"""
import http.client
import requests
"""
lSearch_List = []

iNumParole = int(input("Quante parole ci sono nella matrice? "))
for i in range(iNumParole):
    lSearch_List.append(input("Inserisci parola: "))"""
    
#come fare una riscerca su google di qualcosa e catturane il numero di risultati

connection = http.client.HTTPSConnection("www.google.it")
connection.request("GET", "/")
response = connection.getresponse()
print("Status: {} and reason: {}".format(response.status, response.reason))
print(response.read())
connection.close()