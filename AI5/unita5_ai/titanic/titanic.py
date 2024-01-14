import sys
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import math
from sklearn.model_selection import train_test_split
from sklearn.neighbors import NearestNeighbors
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_recall_fscore_support
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from collections import Counter
from sklearn.model_selection import cross_validate
from procedure import distanza_euclidea

def StampaDataset(dataset):
    dataset.info()
    pd.set_option('display.max_columns', None)
    print(dataset.head(10))
    print(dataset.describe())


def isNaN(string):
    return string != string

training = pd.read_csv('./dataset/train.csv')
test = pd.read_csv('./dataset/test.csv')

#******************************
#rielaborazione delle variabili
#******************************
training = training.drop('Name', axis=1,)
training = training.drop('Ticket', axis=1,)
training = training.drop('Fare', axis=1,)
training = training.drop('Cabin', axis=1,)


training['Family'] = training['SibSp'] + training['Parch'] + 1

training = training.drop('SibSp', axis=1,)
training = training.drop('Parch', axis=1,)

#StampaDataset(training)
#print(training['Embarked'].value_counts())
#Fase di pulizia dei dati
training["Age"] = training["Age"].fillna(training["Age"].median())
training["Embarked"] = training["Embarked"].fillna("S")

#codifica di Emarked
embarke = training["Embarked"].unique()
print(len(embarke))
embarke_rep = []
for i in range(len(embarke)):
    embarke_rep.append(i)
training.Embarked.replace(embarke, embarke_rep, inplace=True)

training.Sex.replace(['male', 'female'], [1,0], inplace=True)
#StampaDataset(training)

#Iniziamo la fase di analisi
X = np.array(training.filter(['Pclass','Sex','Embarked','Family','Age'], axis=1))
y = np.array(training.filter(['Survived'], axis=1))
X_1, X_test, y_1, y_test = train_test_split(X,y, test_size=0.3)
print("Train vector len:" + str(len(X_1)))
print("Test vector len:" + str(len(X_test)))

print("Train vector len (y):" + str(len(y_1)))
print("Test vector len (y):" + str(len(y_test)))

k=6

knn = KNeighborsClassifier(n_neighbors = k, metric=distanza_euclidea)
knn.fit(X_1, y_1.ravel())
pred = knn.predict(X_test)
print("Prima persona:" + str(y_test[0]) + " valore stimato: " + str(pred[0]))

iNumErrori = 0.0
for i in range(len(pred)):
    print("Valore vero:" + str(int(y_test[i])) + " valore stimato: " + str(pred[i]))
    if(int(y_test[i])!=int(pred[i])):
        iNumErrori += 1
print("Num errori: " + str(iNumErrori) + " su " + str(len(pred)))
Qualita = (1.0 - (iNumErrori/len(pred)))*100
print("Bonta dell'algoritmo: " + str(Qualita) + "%")


sys.exit()



training['train_test'] = 1
test['train_test'] = 0


test['Survived'] = np.NaN
all_data = pd.concat([training,test])
#print(all_data.columns)

#training.info()
pd.set_option('display.max_columns', None)
#print(training.head(10))
#print(training.describe())

"""
# seperate the data into numeric and categorical
df_num = training[['Age','SibSp','Parch','Fare']]
df_cat = training[['Survived','Pclass','Sex','Ticket','Cabin','Embarked']]
"""

"""
for i in df_num.columns:
    plt.hist(df_num[i])
    plt.title(i)
    plt.show()
"""


#distribuzione di frequenza
"""
print(training['Survived'].value_counts())
print(training['Pclass'].value_counts())
print(training['Sex'].value_counts())
print(training['Ticket'].value_counts())
print(training['Cabin'].value_counts())
print(training['Embarked'].value_counts())
sys.exit()


sns.heatmap(df_num.corr())
plt.show()
"""

#print(pd.pivot_table(training, index = 'Survived', values = ['Age','SibSp','Parch','Fare']))

#print(pd.pivot_table(training, index = 'Pclass', columns = 'Embarked',
#                     values = 'Ticket' ,aggfunc ='count'))


#for i in range(len(training)):
#    if isNaN(training['Cabin'][i] )==False:
#        print(training['Cabin'][i])
"""
training['cabin_multiple'] = training.Cabin.apply(lambda x: 0 if pd.isna(x)
                                                    else len(x.split(' ')))

training['cabin_adv'] = training.Cabin.apply(lambda x: str(x)[0])

print(training['cabin_adv'].value_counts())


print(pd.pivot_table(training, index = 'Survived', columns = 'cabin_adv',
                     values = 'Ticket' ,aggfunc ='count'))


sys.exit()
"""












