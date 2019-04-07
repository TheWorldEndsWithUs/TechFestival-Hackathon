import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize
from sklearn.pipeline import FeatureUnion
from nltk.corpus import stopwords 
import os
import string

def removeStopWords(wordList):
    return [word for word in wordList if word not in stopwords.words('english')]

# DO NOT USE
def calcCosSimOld(aMat,bVec):
    # Calculate cosine simularity
    a = np.sum(aMat,axis=0)/aMat.shape[0]
    b = bVec.copy()
    return np.dot(a,b)/(np.linalg.norm(a)*np.linalg.norm(b))

def calcCosSim(a,b):
    # Calculate cosine simularity
    return np.dot(a,b)/(np.linalg.norm(a)*np.linalg.norm(b))

def removeStem(sentence):
    ps = PorterStemmer()
    words = word_tokenize(sentence)
    tmpStr = ''
    for w in words:
        tmpStr += ps.stem(w) + ' '
    return tmpStr


rootPath = './company0/'
complaintSubPath = 'complaint/'

contractPath = rootPath + '/termService/' + '0.txt'
#contractPath = rootPath + '/termService/' + 'related.txt'
#contractPath = rootPath + '/termService/' + 'unrelated.txt'

contractTxt = open(contractPath, encoding="utf8", errors='ignore').read()
contractVec = removeStopWords([removeStem(contractTxt)])

vec = CountVectorizer()
contractFreq = vec.fit_transform(contractVec)


compList = []

# Used for removing stem from words
for cFilePath in os.listdir(rootPath + complaintSubPath):
    cFilePath = rootPath + complaintSubPath + cFilePath
    cFileTxt = open(cFilePath,'r').read()

    cFileTxt = removeStem(cFileTxt)

    compList.append(cFileTxt + ' ')

compList = [''.join(str(v) for v in compList)]  # We are combining all complaints into one
complantCnt = CountVectorizer()
a = complantCnt.fit_transform(compList)
#print(contractVec)

resPara = []
resScore = []

splitNum = 500
#for paragraph in contractTxt.split('\n'):
for paragraph in [contractTxt[i:i+splitNum] for i in range(0, len(contractTxt), splitNum)]:
    paragraph = paragraph.translate(string.punctuation)


    try:
        vec = CountVectorizer()
        contractFreq = vec.fit_transform([paragraph])
    except:
        continue
    complaintDf = pd.DataFrame(a.toarray(),columns=complantCnt.get_feature_names())
    contractDf = pd.DataFrame(contractFreq.toarray(),columns=vec.get_feature_names())

    combinedDf = pd.concat([complaintDf, contractDf],sort=False).fillna(value=0.0)
    complainVec = combinedDf.iloc[0].values
    contractVec = combinedDf.iloc[1].values

    simRes = calcCosSim(complainVec,contractVec)
    #print(simRes)
    resPara.append(paragraph)
    resScore.append(simRes)



print(resPara[np.argmax(resScore)])
print('')
print(np.max(resScore))
