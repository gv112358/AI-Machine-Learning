from math import sqrt
from random import randint 

#definiamo una distanza
def distanza_euclidea(row1,row2,n):
    somma = 0.0
    for i in range(n):
        somma += (row1[i] - row2[i])**2
    return sqrt(somma)

def knn_get_neighbours(train,row,k):
    distances = []
    for train_row in train:
        dist = distanza_euclidea(train_row, row,len(row)-1)
        distances.append((train_row, dist))
    distances.sort(key = lambda tup: tup[1])
    ret_rows = []
    for i in range(k):
        ret_rows.append(distances[i][0])
    return ret_rows



def knn_predict(row, train_set, k):
    neighbours = knn_get_neighbours(train_set, row, k)
    output_values = [row[-1] for row in neighbours]
    output_values_set = set(output_values)
    frequenze = {}
    for val in output_values_set:
        frequenze[val] = output_values.count(val)
    return max(frequenze,key=frequenze.get)



#importiamo il dataset
dataset = []
flag = 0
file = open("Iris.csv")
line_vect = []
for line in file:
    if flag != 0:
        line_vect = line.split(",")
        iris_sepal_petal = []
        iris_sepal_petal.append(float(line_vect[1]))
        iris_sepal_petal.append(float(line_vect[2]))
        iris_sepal_petal.append(float(line_vect[3]))
        iris_sepal_petal.append(float(line_vect[4]))
        if line_vect[5] == 'Iris-setosa\n':
            iris_sepal_petal.append(0)
        if line_vect[5] == 'Iris-versicolor\n':
            iris_sepal_petal.append(1)
        if line_vect[5] == 'Iris-virginica\n':
            iris_sepal_petal.append(2)
        dataset.append(iris_sepal_petal)
        
    else:
        flag = 1
file.close()
#definiamo train set e test set
iDimTestSet = int(len(dataset) * 0.1)
VettoreIndici = []
VettoreNumeri = []
for i in range(len(dataset)):
    VettoreNumeri.append(-1)
iNumRandomNumberDifferenti = 0
while(iNumRandomNumberDifferenti<iDimTestSet):
    num = randint(0,len(dataset)-1)
    if VettoreNumeri[num] == -1:
        VettoreNumeri[num] = 1
        VettoreIndici.append(num)
        #VettoreIndici[iNumRandomNumberDifferenti] = num
        iNumRandomNumberDifferenti += 1

TrainSet = []
TestSet = []
for i in range(len(dataset)):
    if i in VettoreIndici:
        TestSet.append(dataset[i])
    else:
        TrainSet.append(dataset[i])

k=5
ret = knn_predict(TestSet[0], TrainSet, k)
print("Valore vero: " + str(TestSet[0][4]) + " Valore stimato: " + str(ret))

iNumErrori = 0.0
for flower in TestSet:
    ret = knn_predict(flower, TrainSet, k)
    if flower[-1] != ret:
        iNumErrori += 1

Qualita = (1.0 - iNumErrori/len(TestSet)) * 100
print("bontà dell'algoritmo: " + str(Qualita) + " %")


#per ogni unità del test set ordiniamo i fiori del train set in base alla distanza
#prendiamo i primi k


