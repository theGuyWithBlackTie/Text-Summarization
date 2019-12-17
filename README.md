# Text-Summarization
This is an extractive based text summarization. This project's idea is inspired from this technical [paper](https://link.springer.com/content/pdf/10.1007%2F978-3-540-88636-5.pdf). You can refer either this paper first to get a deep understanding or either you can read the following text to get a overview.


## Data Used
This project used BBC's news articles taken from [Kaggle](https://www.kaggle.com/pariza/bbc-news-summary/).
Each article in the data set has around 250-500 words and their corresponding summary has around 90-180 words. The ratio of word count between news articles and corresponding summary is around 40%.

## Execution Steps
Following steps are executed in the order mentioned to get the summary:
1. Text Preprocessing
2. Sentence Tokenization & Word Tokenization based on N-grams
3. Calculate TF*IDF score of each word in a sentence
4. Computing cosine-similarities values between each pair of sentences using TF*IDF and compute average for each sentence.
5. Take top K sentences based on cosine-similarity average and get their sentene index
6. Sort the indexes on ascending order and take the sentence from tokenized sentence and put in summary.

## Evaluation Procedure
To evaluate ROGUE metric have been used. Generated summary is compared with dataset's summary.
Depending on the articles'content, the accuracy achieved is from 55% to 80%. Being an extractive summarizer, this accuracy is pretty good.

## Using the Text Summarizer Code
The `main.py` file initiates the code execution. This file calls the other modules (which are memtioned in the Execution Steps section).
Explicitly change in `main.py` value of variable `nGramNumber` to use uni-gram, bi-gram, tri-gram and so on.  

On the similar lines, you can choose how many sentences you want to retain in the summary from the original text by giving values from 0 to 1 in code line `noOfSentences = 0.50*len(tokenizedSentence)` in `main.py` file.  

Original text need to be kept in file; file path mentioned in `main.py`file. And the output is given in another output file again mentioned in `main.py`file. Both files path/name can be changed willingly.
