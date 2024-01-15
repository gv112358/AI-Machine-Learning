import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import sklearn
import sklearn.model_selection
#from sklearn.datasets import load_boston
from sklearn.linear_model import LinearRegression
import sklearn.metrics as metrics
import statsmodels.api as sm
import seaborn as sns
import stat_descr as sd
import sys

def regression_results(y_true, y_pred):
    # Regression metrics
    explained_variance=metrics.explained_variance_score(y_true, y_pred)
    mean_absolute_error=metrics.mean_absolute_error(y_true, y_pred) 
    mse=metrics.mean_squared_error(y_true, y_pred) 
    #mean_squared_log_error=metrics.mean_squared_log_error(y_true, y_pred)
    median_absolute_error=metrics.median_absolute_error(y_true, y_pred)
    r2=metrics.r2_score(y_true, y_pred)

    print('explained_variance: ', round(explained_variance,4))
    #print('mean_squared_log_error: ', round(mean_squared_log_error,4))
    print('r2: ', round(r2,4))
    print('MAE: ', round(mean_absolute_error,4))
    print('MSE: ', round(mse,4))
    print('RMSE: ', round(np.sqrt(mse),4))

print("Programma per la regressione lineare");

dataset = pd.read_csv("appartamenti.csv", sep =",")

X = dataset.drop(['PRICE','Index'], axis = 1)
Y = dataset['PRICE']
"""
Il passaggio successivo è dividere il dataset in TEST E TRAIN
"""
X_train, X_test, Y_train, Y_test = sklearn.model_selection.train_test_split(X, Y, test_size = 0.33, random_state = 5)
lm = LinearRegression()
lm.fit(X_train, Y_train)

#print(type(lm))
#dumpobj(lm);

print("B0 ",round(lm.intercept_,2))
ii=0;
for coef in lm.coef_ :
    print("Var {0} - Coeff {1}".format(X.columns[ii], round(coef,2)))
    ii = ii + 1;

#Y_pred = lm.predict(X_test)
#print(Y.describe());

Y_pred = lm.predict(X_test)

regression_results(Y_test, Y_pred)

sys.exit()



"""

chas0 = dataset[dataset['CHAS']==0.0]
chas1 = dataset[dataset['CHAS']==1.0]

label0 = 'lontano dal fiume'
label1 = 'vicino al fiume'
fig, axes = plt.subplots(nrows=1, ncols=2,figsize=(10, 4))
sns.histplot(chas0['PRICE'],bins=25, ax = axes[0])
sns.histplot(chas1['PRICE'],bins=25, ax = axes[1])
plt.show()
"""


#valori correliati
for col1 in dataset.columns:
    for col2 in dataset.columns:
        if col1 != col2:
            cor = abs(dataset[[col1,col2]]).corr()
            if cor.values[0][1] > 0.6:
                print(cor)






#sd.StampaDataset(dataset)

#istogramma sui prezzi
#dataset.isnull().sum()
"""
sns.set(rc={'figure.figsize':(10,8)})
sns.histplot(dataset['PRICE'], bins=25)
plt.show()
"""
#matrice di correlazione
#print(dataset.corr())
plt.figure(figsize=(20,10))
sns.heatmap(dataset.corr().abs(), annot = True)
plt.show()
#dataset = load_boston(); rimossa da versione 1.2 di scikitlearn
#print(type(dataset));

"""
Nel linguaggio Python i dizionari sono una 
particolare tipologia di variabile vettore che include una 
collezione di oggetti reperibili tramite una chiave. 
A ciascuna chiave corrisponde un valore.
Anche la variabile dataset è un dizionario
"""
#print(dataset.keys());
#print(dataset.feature_names);
#print(dataset['feature_names'])
#print(dataset['DESCR'])

#ci restituisce la dimensione del dataset, con 13 variabili
#print(dataset.data.shape);


#per vedere meglio le caratteristiche del dataset
#print(dataset['DESCR']) da load_boston