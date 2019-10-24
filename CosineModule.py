import numpy as np
from numpy.core._rational_tests import denominator

class CosineSimilarity:
    
    def calculateCosineSimilarity(self,tfIdMatrix):
        print("Nos of rows",np.shape(tfIdMatrix)[0])
        dim = (np.shape(tfIdMatrix)[0], np.shape(tfIdMatrix)[0])
        resultMatrix = np.zeros(dim)
        rowCount = 0
        columnCount = 0
        for eachRow in tfIdMatrix:
            A = eachRow
            columnCount = 0
            for B in tfIdMatrix:
                abDotProduct = np.dot(A,B)
                denominator = np.sqrt(np.dot(A,A)) * np.sqrt(np.dot(B,B))
                cosTheta = abDotProduct/denominator
                resultMatrix[rowCount][columnCount] = cosTheta
                columnCount = columnCount + 1
            rowCount = rowCount + 1
        
        #print(resultMatrix)
        sentenceImportance = {}
        cnt = 0
        for eachRow in resultMatrix:
            sentenceImportance[cnt] = (np.sum(eachRow)/len(eachRow))
            cnt = cnt + 1
        print(sentenceImportance)
        return sentenceImportance