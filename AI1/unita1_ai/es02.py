#import matplotlib
#matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import csv
import sys

iris = []
features = []
with open("iris.csv", "r") as file:
    reader = csv.reader(file)
    items = (riga for riga in reader)
    features = next(items)
    for r in items:
        iris.append(r)
    

print(features)


def PrendiDa1a4(l):
    return l[1:5]

def Prendi5(l):
    return l[5]
target = list(map(Prendi5, iris))

data = list(map(PrendiDa1a4, iris))
data=list(map(lambda v: list(map(lambda x: float(x), v)), data))
target = list(map(Prendi5, iris))

print(data)
print(target)

fig, ax = plt.subplots()
colors = ['blue', 'red', 'green']

for label, color in zip(range(len(target)), colors):
    ax.hist(data[0], 
            label=target[label],
            color=color)

ax.set_xlabel(features[0])
ax.legend(loc='upper right')

plt.show()

sys.exit(0)