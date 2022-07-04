import unicodecsv
import random
import operator
import math
import pandas as pd
import csv
import matplotlib.pyplot as plt

def loadData(filename):
    with open (filename, 'r') as csvfile:
        lines = csv.reader(csvfile, delimiter = ',')
        data = list(lines)
    return data



def splitData(filename, percentageTrainingSetData, percentageTestSetData):
    data = loadData(filename)
    random.shuffle(data)
    testSetData = data[:int((len(data)*percentageTestSetData)/100):]
    trainingSetData = data[:int((len(data)*percentageTrainingSetData)/100)]

    return trainingSetData, testSetData

#Euclidian distance function
def euclidianDist(instance1, instance2):
    distance = 0.0

    for x in range((len(instance1)-1)):
        distance+=(pow(((float(instance1[x]))-(float(instance2[x]))),2) ) #Euclidian distance calculator
    return math.sqrt(distance)

#KNN Algorithm function
def knn(trainingSetData, testSetData, k):
    neighbors = []  # Will contain the label of the k nearest neighbors for all the test data points

    for i in (testSetData):
        distances = []  # Contains all euclidians distances calculated
        knn = [] 

        for j in (trainingSetData) :
            i_value = i[0].split(" ") #Retrieve the values of the coordinate i in a list
            j_value = j[0].split(" ") #Retrieve the values of the coordinate i in a list
            dist = euclidianDist(i_value, j_value)
            distances.append(((j_value[2]),dist))
            distances.sort(key=operator.itemgetter(1))
            knn = distances[:k] #Retrieve the k smallest distances which correspond to the k nearest neighbors

        lines = [] #Will contain the set label of the k nearest neighbors for each test data points
        for x in range(len(knn)):
            lines.append(knn[x][0])
        neighbors.append(lines)
    return neighbors

#Classifier decision function
def getDominantClass(set_labels):
    class1=0
    class2=0
    class3=0
    class4=0

    for k in range(len(set_labels)):
        if (set_labels[k]=='1'):
            class1+=1
        elif (set_labels[k]=='2'):
            class2+=1
        elif (set_labels[k]=='3'):
            class3+=1
        elif (set_labels[k] == '4'):
            class4+=1
    if (class1>class2 and class1>class3 and class1>class4): #class 1 is the dominant class
        return 1
    elif (class2>class1 and class2>class3 and class2>class4): #class 2 is the dominant class
        return 2
    elif (class3>class1 and class3>class2 and class3>class4): #class3 is the dominant class
        return 3
    elif (class4>class1 and class4>class2 and class4>class3): #class4 is the dominant class (only for the base3)
        return 4
    else :          #equi-representation case, return -1
        return (-1)

#Return true or false if expected_label and predicted_label are equals or not
def check_result(expected_data, predicted_label):
    if (expected_data == predicted_label) :
        return True
    elif (expected_data != predicted_label) :
        return False

#Return the confusion matrice
def confusion_matrix(trainingSetData, testSetData, k):
    cm = [] #Confusion matrice
    predicted_labels = [] #Will contains the predicted labels or dominant class obtained after applying knn for each test data points
    expected_labels =  [] #Will contains the expected labels or dominant class of the test data points
    neighbors = knn(trainingSetData, testSetData, k)
    #print(testSetData[])

    for i in range(len(testSetData)):
        predicted_labels.append(getDominantClass(neighbors[i]))

    for j in testSetData:
        j_value = j[0].split(" ")
        expected_labels.append(j_value[2])

    accuracy = getAccuracy(testSetData,predicted_labels)

    #Lets draw the confusion matrix
    for l in range(3):
     cm.append([0]*3) #Confusion matrice initialized to 0

    for m in range (len(testSetData)):
        if (check_result(int(expected_labels[m]),int(predicted_labels[m])) == True):
            cm[int(expected_labels[m])-1][int(predicted_labels[m])-1]+=1
        elif (check_result(int(expected_labels[m]),int(predicted_labels[m])) == False):
            cm[int(expected_labels[m])-1][int(predicted_labels[m])-1]+=1

    return cm, accuracy

def getAccuracy (setData, predictions):
    correct=0
    for i in range(len(setData)):
        expected_label=setData[i][0].split(" ")
        if ((check_result(int(expected_label[2]),int(predictions[i])) == True)):
            correct+=1

    return (correct/float(len(setData)))

#Generate plot
def graph (nbOfSetData, accuracy):
    plt.plot(nbOfSetData,accuracy,label = 'Number of learning examples / Recognition rate')

    plt.legend()
    plt.xlabel('Number of learning examples')
    plt.ylabel('Recognition Rate')
    plt.show()

nbOfSetData= []
accuracyTable = []
for i in (10,20,30,40,50,60,70,80,90,100):
    trainingSetData, testSetData = splitData('base2.txt',100,i)
    print('The training setData is',len(trainingSetData))
    print('The test setData is',len(testSetData))
    cm, accuracy = confusion_matrix(trainingSetData,testSetData,1)

    nbOfSetData.append(len(testSetData))
    accuracyTable.append(accuracy)

    print(cm[0])
    print(cm[1])
    print(cm[2])
    #print(cm[3])

#print(nbOfSetData)
#print(accuracyTable)
graph(nbOfSetData,accuracyTable)
#testSet=[[1, 1, 1, 'a']], [[2,2,2],'a'], [[3,3,3],'b']
#predictions = ['a','a','a']
#accuracy=getAccuracy(testSet,predictions)
#print('The confusion matrix for k = 4 is')
#print(cm[0])
#print(cm[1])
#print(cm[2])
#print(cm[3])
#trainingSetData, testSetData = splitData('base1.txt')
#cm = confusion_matrix(trainingSetData,testSetData,7)
#print('The confusion matrix for k = 7 is')
#neighbors=
#knn(trainingSetData,testSetData,5)
#print(neighbors)

#dominant = getDominantClass(neighbors)
#print('The dominant class is the class',dominant)
