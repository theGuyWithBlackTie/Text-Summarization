from textProcessingModule import *
from Ngrams import *
from TfIdfModule import *
from CosineModule import CosineSimilarity
from operator import itemgetter

file = 'data\\text\\005.txt'
file = open(file, 'r')
text = file.read()

nGramNumber = 3
'''
Pre-processing of the Text
'''
textProcessing = TextProcessing()
tokenizedSentence = textProcessing.sentenceTokenization(text)

noOfSentences = 0.50*len(tokenizedSentence)
#print(tokenizedSentence)

text = textProcessing.preprocessText(text)
tokenizedWords = textProcessing.tokenizing(text)


nGrams = Ngrams()
#print("tokenizedWords ->",tokenizedWords)
tokenizedWordsWithNGrams = nGrams.generate_ngrams(tokenizedWords, nGramNumber)
#print(tokenizedWordsWithNGrams)

tfId = TfIdf(nGramNumber)
tfIdMatrix = tfId.calculateTfIdfMatrix(tokenizedWordsWithNGrams, tokenizedSentence)

#print(tfIdMatrix)
outF = open('output.txt',"w")
outF.write(tfIdMatrix.__str__())

cosine = CosineSimilarity()
sentenceImportanceValues = cosine.calculateCosineSimilarity(tfIdMatrix)

sentenceImportanceValues = sorted(sentenceImportanceValues.items(), key = itemgetter(1), reverse=True)
##print(sentenceImportanceValues)

cnt = 0
sentenceNo = []

#print("no. of sentences ->",noOfSentences)

for sentence_prob in sentenceImportanceValues:
    if cnt <= noOfSentences:
        sentenceNo.append(sentence_prob[0])
        cnt = cnt + 1
    else:
        break

sentenceNo.sort()
#print(sentenceNo)

summary = []
#print("Sentence->",tokenizedSentence)

for value in sentenceNo:
    summary.append(tokenizedSentence[value])

summary = " ".join(summary)
outF = open('summary.txt',"w")
outF.write(summary)




