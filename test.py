import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
from nltk.corpus import stopwords

def removeStopWords(wordList):
    return [word for word in wordList if word not in stopwords.words('english')]

def calcCosSim(aMat,bVec):
    # Calculate cosine simularity
    a = np.sum(aMat,axis=0)/aMat.shape[0]
    b = bVec.copy()
    return np.dot(a,b)/(np.linalg.norm(a)*np.linalg.norm(b))



docs = ['why hello there', 'omg hello pony', 'she went there? omg']

docsFiltered = removeStopWords(docs)

vec = CountVectorizer()
X = vec.fit_transform(docsFiltered)

a = X.toarray()

test = [0,0,0,1,0,0,1]
res = calcCosSim(a,test)

print(a)
print(res)



#df = pd.DataFrame(X.toarray(), columns=vec.get_feature_names())
#print(df)
#vec.get_feature_names()
