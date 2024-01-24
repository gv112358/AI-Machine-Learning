import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import sklearn
import sklearn.model_selection
from sklearn.linear_model import LinearRegression
import sklearn.metrics as metrics
import statsmodels.api as sm
import seaborn as sns
import stat_descr as sd
import sys
from scipy.cluster.hierarchy import linkage
from scipy.cluster.hierarchy import dendrogram
from scipy.cluster.hierarchy import cut_tree


print("Programma per la Cluster Analysis")

dataset = pd.read_csv("Mall_Customers.csv", sep=",")

#numericDataset = dataset._get_numeric_data()
#print(numericDataset.head(20))

#sd.StampaMatriceCorrelazioneNew(dataset)
#sd.StampaHeatMap(dataset)

#dataset = dataset.drop('CustomerID', axis=1)
dataset.drop('CustomerID', axis=1, inplace= True)
dataset_std = sd.StandardizeData(dataset)
#mall_df1 = df.DataFrame(dataset_std, colums)
plt.figure(figsize=(20,10))
mergings = linkage(dataset_std, method='single', metric='euclidean')
dendrogram(mergings)
plt.show()
sys.exit()

sd.StampaMatriceCorrelazione(dataset)

sys.exit()
# sd.StampaDataset(dataset)

# sd.CalcolaIstogramma(dataset,'Gender',2)

# sd.Hist_compare(dataset,"Age","Gender",25)

class_vect = [10, 40, 70, 100, 130, 160]
sd.classify(dataset, class_vect, "Annual Income (k$)", "Income_new")

# print(dataset[["CustomerID", "Annual Income (k$)", "Income_new"]])

# sd.Hist_compare(dataset,"Age","Income_new",25)
