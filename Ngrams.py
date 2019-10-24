class Ngrams:
    
    def generate_ngrams(self,listOfWords, n):
        nGramsList = []
        for num in range(0, len(listOfWords)):
            nGramWord = ' '.join(listOfWords[num:num+n])
            nGramsList.append(nGramWord)
        return nGramsList