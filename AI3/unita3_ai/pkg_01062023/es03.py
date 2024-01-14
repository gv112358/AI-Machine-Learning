import requests
from random import *
import warnings
import os



"""
**********************************************
PROGRAMMA CHE IMPLEMENTA LA DISTANZA DI GOOGLE
**********************************************

Prerequisiti
pip3 install selenium
brew install --cask chromedriver
usr/local/bin/chromedriver    è il path dove è installato di default chromedriver

Al primo lancio l'applicazione viene bloccata.
Bisogna andare su PREFERENZE DI SISTEMA (MAC) -> SICUREZZA E PRIVACY -> GENERALI
e li consentire dove si fa riferimento al blocco dell'app

Aggiornamento 2023
Da terminale : 

wget -nc https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb 

sudo apt update 
sudo apt install -f ./google-chrome-stable_current_amd64.deb

pip3 install -U selenium
pip3 install webdriver-manager

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_argument("start-maximized")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://www.google.com%22/)

"""




from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = None
sPre = "'"
sCentral = "' + '"
sPost = "'"




def EstraiNumeroRisultati(sAppo):
    #sAppo = "Circa 3.670.000 risultati (0,55 secondi)"
    iIndex = sAppo.find(" ")
    sAppo = sAppo[iIndex + 1:]
    iIndex = sAppo.find(" ")
    sAppo = sAppo[0:iIndex]
    sAppo = sAppo.replace(",","")
    iAppo = int(sAppo)
    #print("ciao " + str(iAppo + 1)) 
    return iAppo

def InitGoogleDriver():
    global driver
    driver = webdriver.Chrome('/usr/local/bin/chromedriver')



def GetGoogleSearchResult(sStrToSearch):
    global driver
    driver.get("https://www.google.it/search?q=" + sStrToSearch)
    sAppo = driver.find_element("id", "result-stats")
    #print(sAppo.text)
    return EstraiNumeroRisultati(sAppo.text)
    #search_bar = driver.find_element_by_name("q")
    #search_bar.clear()
    #search_bar.send_keys("getting started with python")
    #search_bar.send_keys(Keys.RETURN)
    #print(driver.current_url)

def EndGoogleDriver():
    global driver
    driver.close()


def send_request(sStrToSearch):
    response = requests.get(
        url="https://app.scrapingbee.com/api/v1/store/google",
        params={
            "api_key": "9L0VSCBE6299Y18SAGKE0ABRIS86IOD0JOBQVN5JSA9BQKJKJC9WEBWXAFPQLFHJYXPIB4I1QGWFEARN",
            "search": sStrToSearch,
        },

    )
    print('Response HTTP Status Code: ', response.status_code)
    if(response.status_code==200):
        buf = response.content
        pos = buf.find(b'number_of_results')
        if(pos > 0): 
            pos_end = buf.find(b',', pos)
            print(int(buf[pos + 20:pos_end]))
            return int(buf[pos + 20:pos_end])

    return -1
        


def levenshtein(s1, s2):
    if len(s1) < len(s2):
        s1, s2 = s2, s1

    if len(s2) == 0:
        return len(s1)

    previous_row = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row

    #return previous_row[-1]/float(len(s1))
    return previous_row[-1]


#Come prima cosa dobbiamo chiedere le chiavi rispetto alle quali
#costruiamo la matrice delle distanze

#EstraiNumeroRisultati()
#exit(0)



print("\n\nINIZIO PROGRAMMA")
search_list = [];
mydict = {}
iNumChiavi = int(input("Inserisci il numero di chiavi: "))
print("Hai richiesto " + str(iNumChiavi) + " chiavi")
for ii in range(iNumChiavi):
    sAppo = input("Inserisci chiave " + str(ii) + ": ")
    search_list.append(sAppo)

InitGoogleDriver()
for ii in range(iNumChiavi):
  for jj in range(ii,iNumChiavi):
    if(ii == jj):
      #print("Dobbiamo cercare " + search_list[ii])
      sAppo = sPre + search_list[ii] + sPost
      iAppo = GetGoogleSearchResult(sAppo)
      mydict[sAppo] = iAppo
      print("Cercato " + sAppo + " " + str(iAppo))
    else:
      #print("Dobbiamo cercare " + search_list[ii] + " " + search_list[jj])
      sAppo = sPre + search_list[ii] + sCentral + search_list[jj] + sPost
      iAppo = GetGoogleSearchResult(sAppo)
      mydict[sAppo] = iAppo
      print("Cercato " + sAppo + " " + str(iAppo))
EndGoogleDriver()

print("Inizio calcolo matrice")
for ii in range(iNumChiavi):
    for jj in range(ii,iNumChiavi):
        if(ii == jj):
            sAppo = sPre + search_list[ii] + sPost
            #print("Risultati per " + sAppo + " " + str(mydict[sAppo]))   
            sAppo1 = sAppo
            sAppo2 = sAppo 
        else:
            sAppo = sPre + search_list[ii] + sCentral + search_list[jj] + sPost
            #print("Risultati per " + sAppo + " " + str(mydict[sAppo]))
            sAppo1 = sPre + search_list[ii] + sPost
            sAppo2 = sPre + search_list[jj] + sPost
        iMin = min(mydict[sAppo1],mydict[sAppo2])
        iMin = iMin/2
        if(mydict[sAppo]>iMin):
            iDist = 0
        else:    
            iDist = 1 - mydict[sAppo]/iMin;
        if(sAppo1 != sAppo2):    
            print("La dist tra " + sAppo1 + " e " + sAppo2 + ":" + str(iDist))