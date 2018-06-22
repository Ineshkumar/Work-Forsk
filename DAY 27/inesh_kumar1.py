# -*- coding: utf-8 -*-
"""
Created on Mon Jun 18 12:33:38 2018

@author: inesh
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Jun 18 11:10:22 2018

@author: inesh
"""

import pandas as pd
data=pd.read_csv('/media/inesh/f32962a9-22d0-44de-adc0-8bb316305013/forsk/DAY 27/movie.csv')

import re
import nltk

nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
crpus=[]
for i in range(0,2000):
    review=re.sub('[^a-zA-Z]',' ',data['text'][i])
    review=review.lower()
    review=review.split()
    ps=PorterStemmer()
    review = [ps.stem(word) for word in review if not word in set(stopwords.words('english'))]
    review = ' '.join(review)
    crpus.append(review)

from sklearn.feature_extraction.text import CountVectorizer
cv=CountVectorizer(max_features=2500)
features = cv.fit_transform(crpus).toarray()
labels = data.iloc[:,0].values     


from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
labels=le.fit_transform(labels)


from sklearn.cross_validation import train_test_split
features_train,features_test,labels_train,labels_test=train_test_split(features,labels,test_size=0.20,random_state=0)    


from sklearn.naive_bayes import GaussianNB
classifier=GaussianNB()
classifier.fit(features_train,labels_train)
labels_predi=classifier.predict(features_test)
from sklearn.metrics import confusion_matrix, accuracy_score
cm=confusion_matrix(labels_test,labels_predi)
score=accuracy_score(labels_test, labels_predi)



from sklearn.ensemble import RandomForestClassifier
regressor=RandomForestClassifier(n_estimators=100,random_state=0)
regressor.fit(features_train,labels_train)
labels_predi1=classifier.predict(features_test)
from sklearn.metrics import confusion_matrix, accuracy_score
cm1=confusion_matrix(labels_test,labels_predi1)
score1=accuracy_score(labels_test, labels_predi1)


