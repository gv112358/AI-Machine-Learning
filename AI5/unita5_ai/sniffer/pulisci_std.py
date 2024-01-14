import math
import sys
import os
import os.path
import pandas as pd
from pandas import DataFrame, read_csv
import time
import dbclient as db

#sys.path.insert(1, '/Users/andrea/Progetti/pythonMAC/Librerie')
#import dataframe as mydf
#import filelog as fl

sQueryPerCheckDK = "select Description,Quantity,InvoiceDate,Price,CustomerID,Country,InvoiceTime from ordini where "


def exit():
	sys.exit(0);



def StampaDataFrame(dfDataframeToPrint):
	print("StampaDataFrame: richiamata procedura");
	count_row = dfDataframeToPrint.shape[0]
	count_col = dfDataframeToPrint.shape[1]
	#print("Righe e colonne: ",count_row,count_col);
	with pd.option_context('display.max_columns',40):
		print(dfDataframeToPrint.info())
		print(dfDataframeToPrint.describe())
		print(dfDataframeToPrint.head(5))


def SplitDataframe(dfData, sBaseName):
	sBaseName = sBaseName.replace(" ", "_").replace("-", "_")
	len = dfData.shape[0]
	i = 0
	step = 10000
	while (i < len):
		if (i + step <= len):
			df1 = dfData[i:i + step]
			sFilename = "./csv/" + sBaseName + "_" + str(i) + "_" + str(i + step - 1) + ".csv"
		else:
			df1 = dfData[i:len]
			sFilename = "./csv/" + sBaseName + "_" + str(i) + "_" + str(len - 1) + ".csv"

		df1.to_csv(sFilename, index=False)
		i = i + step

def GestisciDuplicateKey(values):
	global cur
	sQueryNow = f" Invoice={values[0]} and StockCode={values[1]};"
	sQuery = sQueryPerCheckDK + sQueryNow
	db.read_in_db(cur,sQuery)


print("Inizio programma gestione file excel")
cur = db.connect()
if cur is None:
	print("Errore connessione al DB")
	exit()
sQueryStart = "insert into ordini(Invoice,StockCode,Description,Quantity,InvoiceDate,Price,CustomerID,Country,InvoiceTime) values "
sQueryEnd =  " on conflict(Invoice,StockCode) do update set Quantity = excluded.Quantity + ordini.Quantity;"

# r=root, d=directories, f = files
for r, d, f in os.walk("./csv"):
	for file in sorted(f):
		if file.endswith(".csv"):
			print("Inizio lettura file " + os.path.join(r, file))
			df = pd.read_csv(os.path.join(r, file), header=0, sep=",")
			for i in range(0,len(df.values)):
				#print(df.values[i])
				if math.isnan(df.values[i][6]):
					iClientID = 0
				else:
					iClientID = df.values[i][6]

				data_ora = df.values[i][4].split(" ")

				#correzione apostrofo + gestione nan
				if(type(df.values[i][2]) == str):
					descrizione = df.values[i][2].replace("'","''")
				else:
					descrizione = "nd"

				if(type(df.values[i][7]) == str):
					country = df.values[i][7].replace("'","''")
				else:
					country= "nd"

				dati = f"('{df.values[i][0]}','{df.values[i][1]}','{descrizione}',{df.values[i][3]},TO_DATE('{data_ora[0]}','YYYY-MM-DD'),{df.values[i][5]},{int(iClientID)},'{country}','{data_ora[1]}') "
				sqlQuery = sQueryStart + dati + sQueryEnd
				ret = db.write_in_db(cur,sqlQuery)
				if(ret != 0):
					filedest = os.path.join(r, file) + ".ok"
					os.rename(os.path.join(r, file), filedest)
					exit()
				#if(ret == -2):
				#	cur = db.connect()
			print(os.path.join(r, file))
			filedest = os.path.join(r, file) + ".ok"
			os.rename(os.path.join(r, file), filedest)
			exit()


"""
cur = db.connect()
sql_insert = "insert into ordini values "
dati = "(1200,'10489434', '85048', '15CM CHRISTMAS GLASS BALL 20 LIGHTS', 12, TO_DATE('2009/12/03','YYYY/MM/DD'), 6.95, 13085, 'United Kingdom', '07:45');"
sql_insert += dati
db.write_in_db(cur,sql_insert)
db.read_in_db(cur,"select * from ordini;")
db.close(cur)
exit()
"""

#fl.LogInit("./filelog21032022.txt","w")
file_excel = pd.ExcelFile('./online_retail_II.xlsx');
print(type(file_excel))
for sheet in file_excel.sheet_names:
	print(sheet);

df = file_excel.parse(file_excel.sheet_names[0])
#StampaDataFrame(df)
SplitDataframe(df,"retail")

#fl.LogEnd()	
sys.exit(0)












