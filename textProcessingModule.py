from nltk.stem import WordNetLemmatizer
from nltk.tokenize import sent_tokenize,word_tokenize
from nltk.corpus import stopwords
import re

class TextProcessing:
    
    stopWords = []
    wordLemmatizer = []
    def __init__(self):
        self.stopWords = set(stopwords.words('english'))
        self.wordLemmatizer = WordNetLemmatizer()
    
    def preprocessText(self, text):
        processedText = self.remove_special_characters(str(text))
        processedText = re.sub(r'\d+', '', processedText)
        return processedText
    
    def remove_special_characters(self,text):
        regex = r'[^a-zA-Z0-9\s]'
        text = re.sub(regex,'',text)
        return text
    
    def tokenizing(self,text):
        tokenized_words_with_stopwords = word_tokenize(text)
        tokenized_words = [word for word in tokenized_words_with_stopwords if word not in self.stopWords]
        tokenized_words = [word for word in tokenized_words if len(word) > 1]
        tokenized_words = [word.lower() for word in tokenized_words]
        return tokenized_words
    
    def sentenceTokenization(self,text):
        return sent_tokenize(text)
    
    def removingStopWordsFromSentence(self,sentence):
        tokenize_words_with_stopwords = word_tokenize(sentence)
        tokenized_words = [word for word in tokenize_words_with_stopwords if word not in self.stopWords]
        tokenized_words = [word for word in tokenized_words if len(word) > 1]
        tokenized_words = [word.lower() for word in tokenized_words]
        
        sentence = ' '.join(tokenized_words)
        return sentence