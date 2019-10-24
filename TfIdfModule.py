import numpy as np
from textProcessingModule import *
from Ngrams import *
import nltk
import math

class TfIdf:
    cleaningData =None
    sizeOfEachRow = None
    nGrams = None
    nGramNumber = None
    
    def __init__(self, nGramNumber):
        self.cleaningData = TextProcessing()
        self.nGrams = Ngrams()
        self.nGramNumber = nGramNumber
            
    def calculateTfIdfMatrix(self,words,sentences):
        wordFreq = self.frequencyOfWords(words)
        
        #Clean the tokenized Sentence
        sentences = self.cleanSentence(sentences)
        #print(sentences)
        self.sizeOfEachRow = self.countSizeOfEachRow(sentences)
        tfIdfMatrix = np.empty([len(sentences),self.sizeOfEachRow])
        
        cnt = 0
        for sent in sentences:
            tfIdfMatrix[cnt] = self.sentenceTFIDFValues(sent,wordFreq,sentences)
            cnt = cnt + 1
        
        return tfIdfMatrix
    
    
    def sentenceTFIDFValues(self,sent,wordFreq,sentences):
        eachRowOfMatrix = np.zeros(self.sizeOfEachRow)
        posTaggedSentence = self.posTagging(sent)
        cnt = 0
        for word in posTaggedSentence:
            if word.lower() not in self.cleaningData.stopWords and word not in self.cleaningData.stopWords and len(word) > 1:
                word = word.lower()
                #word = nltk.WordNetLemmatizer.lemmatize(word)
                eachRowOfMatrix[cnt] = self.wordTFID(wordFreq, word, sent, sentences)
                cnt  = cnt + 1
        #print(eachRowOfMatrix)
        return eachRowOfMatrix
    
    def countSizeOfEachRow(self,sentences):
        maxSize = 0
        for eachSentence in sentences:
            size = len(re.findall(r'\w+', eachSentence))
            if(size > maxSize):
                maxSize = size
        return maxSize
    
    def wordTFID(self,wordFreqDict, eachWord, eachSentence, sentences):
        tf = self.tfScore(eachWord, eachSentence)
        idf = self.idfScore(eachWord,sentences)
        return tf*idf
    
    
    
    def tfScore(self, word, sentence):
        wordFreqInSentence = 0
        sentenceInNGrams = self.nGrams.generate_ngrams(sentence.split(), self.nGramNumber)
        for eachWord in sentenceInNGrams:
            if word == eachWord:
                wordFreqInSentence = wordFreqInSentence + 1
        tf = wordFreqInSentence / len(sentenceInNGrams)
        return tf
            
    def idfScore(self,word, sentences):
        noOfSentencesContainingWord = 0
        for eachSentence in sentences:
            eachSentenceInNGrams = self.nGrams.generate_ngrams(eachSentence.split(), self.nGramNumber)
            for eachWord in eachSentenceInNGrams:
                if word == eachWord:
                      noOfSentencesContainingWord = noOfSentencesContainingWord + 1
                      break
        
        idf = math.log10(len(sentences)/noOfSentencesContainingWord)
        return idf



    def posTagging(self,text):
        posTag = nltk.pos_tag(self.nGrams.generate_ngrams(text.split(), self.nGramNumber))
        posTaggedNounVerb = []
        for word,tag in posTag:
            if tag == "NN" or tag == "NNP" or tag == "NNS" or tag == "VB" or tag == "VBD" or tag == "VBG" or tag == "VBN" or tag == "VB"or tag == "VBZ":
                posTaggedNounVerb.append(word)
        return posTaggedNounVerb
    
    
    
    def frequencyOfWords(self,words):
        words = [word.lower() for word in words]
        dict_freq = {}
        words_unique = []
        for word in words:
            if word not in words_unique:
                words_unique.append(word)
                
        for word in words_unique:
            dict_freq[word] = words.count(word)
            
        return dict_freq
    
    def cleanSentence(self,sentences):
        returnSentences = []
        for eachSentence in sentences:
            eachSentence = self.cleaningData.preprocessText(eachSentence)
            eachSentence = self.cleaningData.removingStopWordsFromSentence(eachSentence)
            returnSentences.append(eachSentence)
        return returnSentences