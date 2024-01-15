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

def StampaDataset(dataset):
    dataset.info()
    pd.set_option('display.max_columns', None)
    print(dataset.head(10))
    print(dataset.describe())


def isNaN(string):
    return string != string

def CalcolaIstogramma(dataset, sNomeVar, iBin=25):
    sns.set(rc={'figure.figsize':(10,8)})
    sns.histplot(dataset['sNomevar'], bins=iBin)
    plt.show()

"""
def classify(dataset,class_vect,label,label_new):
    training[label_new] = training.loc[:, label]
    for index, row in dataset.iterrows():
        dataset.at[index, 'Age_new'] = -1
        for jj in range(len(class_vect) - 1):
            if row[label] >= class_vect[jj] and row[label] < class_vect[jj + 1]:
                dataset.at[index, 'Age_new'] = jj
        if row[label] >= class_vect[len(class_vect) - 1]:
            dataset.at[index, 'Age_new'] = len(class_vect) - 1
"""