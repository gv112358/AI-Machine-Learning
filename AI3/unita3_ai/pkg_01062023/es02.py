"""from selenium import webdriver
from selenium.webdriver.common.keys import Keys"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.google.com")

"""def InitGoogleDriver():
    global driver
    driver = webdriver.Chrome('/usr/local/bin/chromedriver')"""

def GetGoogleSearchResult(sStrToSearch):
    global driver
    driver.get("https://www.google.it/search?q=" + sStrToSearch)
    sAppo = driver.find_element("id", "result-stats")
    print(sAppo.text)
    #return EstraiNumeroRisultati(sAppo.text)
    #search_bar = driver.find_element_by_name("q")
    #search_bar.clear()
    #search_bar.send_keys("getting started with python")
    #search_bar.send_keys(Keys.RETURN)
    #print(driver.current_url)

def EndGoogleDriver():
    global driver
    driver.close()

def InitGoogleDriver():
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

#InitGoogleDriver()
GetGoogleSearchResult("Paperino")
EndGoogleDriver()