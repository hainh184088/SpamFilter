# spam filtering with naive bayes
# data proprietary belongs to http://www.dt.fee.unicamp.br/~tiago/smsspamcollection/

import pandas as pd
import numpy as numpy


def load_data(data_path):
    smsDict = pd.read_csv(data_path, sep = '\t', header = None, names = ['Label','SMS'])
    dataRandomized = smsDict.sample(frac = 1,random_state = 1)
    training_test_index = round(len(dataRandomized) * 0.8)
    testSet = dataRandomized[training_test_index:].reset_index(drop = True)
    trainingSet = dataRandomized[:training_test_index].reset_index(drop = True)
    return testSet, trainingSet

def createVocab(trainingSet):
    trainingSet['SMS'] = trainingSet['SMS'].str.replace('\W', ' ') #remove punctuation
    trainingSet['SMS'] = trainingSet['SMS'].str.lower()
    trainingSet['SMS'] = trainingSet['SMS'].str.split()
    vocabulary = []
    for sms in trainingSet['SMS']:
        for word in sms:
            vocabulary.append(word)

    vocabulary = list(set(vocabulary))
    return(vocabulary)

def count(listVocab):
    wordCountsPerSms = {uniqueWord: [0] * len(trainingSet['SMS']) for uniqueWord in listVocab}

    for index, sms in enumerate(trainingSet['SMS']):
        for word in sms:
            wordCountsPerSms[word][index] += 1
    wordCounts = pd.DataFrame(wordCountsPerSms)
    return wordCounts

def clean:
    training_set_clean = pd.concat([training_set, word_counts], axis=1)
    training_set_clean.head()


if __name__ == '__main__':
    testSet,trainingSet = load_data(data_path='./SMSSpamCollection')
    vocabulary = createVocab(trainingSet)
    wordCounts = count(vocabulary)
