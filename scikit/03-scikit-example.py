import numpy as np
import operator
from os import listdir

def CreateDataSet():
    group = np.array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    labels = ['A' , 'A' ,'B' ,'B']
    return group
def Classify(inX, dataSet, labels, k):
    dataSetSize        = dataSet.shape[0]
    diffMat            = np.tile(inX,(dataSetSize,1)) - dataSet
    sqDiffMat          = diffMat ** 2
    sqDistances        = sqDiffMat.sum(axis  = 1) 
    distance           = sqDistances ** 0.5
    sortedDistIndicies = sqDistances.argsort()
    classCount={}
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
    sortedClassCount = sorted(classCount.items(),
                              key = operator.itemgetter(1), reverse = True)
    return sortedClassCount[0][0]

data = CreateDataSet()

Classify(0.5, data, 'C', 2)