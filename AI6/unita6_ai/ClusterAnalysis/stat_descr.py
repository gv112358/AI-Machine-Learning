import sys
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import math
from math import sqrt
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
from sklearn.preprocessing import StandardScaler

def StampaDataset(dataset):
    dataset.info()
    pd.set_option('display.max_columns', None)
    print(dataset.head(10))
    print(dataset.describe())


def isNaN(string):
    return string != string

def CalcolaIstogramma(dataset, sNomeVar, iBin=25):
    sns.set(rc={'figure.figsize':(10,8)})
    sns.histplot(dataset[sNomeVar], bins=iBin) #controlla apici sNomevar
    plt.show()


def classify(dataset, class_vect, label, label_new):
    dataset[label_new] = dataset[label]
    for index, row in dataset.iterrows():
        dataset.at[index, label_new] = -1
        for jj in range(len(class_vect) - 1):
            if row[label] >= class_vect[jj] and row[label] < class_vect[jj + 1]:
                dataset.at[index, label_new] = jj
        if row[label] >= class_vect[len(class_vect) - 1]:
            dataset.at[index, label_new] = len(class_vect) - 1


def Hist_compare(dataset,var1,Classifier,nbins):
   
    Classifier_vect = dataset[Classifier].unique()
    color_vect = ["blue", "purple", "orange", "red", "yellow"]
    #fig, axes = plt.subplots(nrows=1, ncols=2,figsize=(10, 4))
    fig, axes = plt.subplots(nrows=1, ncols=len(Classifier_vect), figsize=(5*len(Classifier_vect), 4))

    for i in range(len(Classifier_vect)):

        Classifier1 = dataset[dataset[Classifier] == Classifier_vect[i]]

        ax = sns.histplot(Classifier1[var1], bins=nbins, label=var1, ax=axes[i], color = color_vect[i%5], kde=False)

        ax.legend()
        ax.set_title(Classifier_vect[i])

    plt.show()

def StampaMatriceCorrelazione(dataset):
    print(dataset.corr())

def StampaMatriceCorrelazioneNew(dataset):
    df_new = dataset._get_numeric_data()
    pd.set_option('display.max_columns', None)
    print(df_new.corr())

def StampaHeatMap(dataset):
    df_new = dataset._get_numeric_data()
    num_var = df_new.shape[1]
    plt.figure(figsize=(num_var,num_var))
    sns.heatmap(df_new.corr(), annot = True, cmap="rainbow")
    plt.savefig('Correlation')
    plt.show()

def StandardizeData(dataset):
    df_new = dataset._get_numeric_data()
    scaler = StandardScaler()
    df_new_scaled = scaler.fit_transform(df_new)
    return df_new_scaled