Recognizing Handwritten Digits with Scikit-Learn

1. Decision Tree Algorithm
"""

from sklearn import datasets
digits = datasets.load_digits()

digits.images.shape

import matplotlib.pyplot as plt
fig, axes = plt.subplots(10, 10, figsize=(8, 8),subplot_kw={'xticks':[], 'yticks':[]},gridspec_kw=dict(hspace=0.1, wspace=0.1))
for i, ax in enumerate(axes.flat):
    ax.imshow(digits.images[i], cmap='binary', interpolation='nearest')
    ax.text(0.05, 0.05, str(digits.target[i]),transform=ax.transAxes, color='green')

X = digits.data
X.shape

y=digits.target
y.shape

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y,test_size=0.2,random_state=0)

X_train.shape

y_train.shape

from sklearn.tree import DecisionTreeClassifier
clf=DecisionTreeClassifier()
clf.fit(X_train,y_train)

y_pred=clf.predict(X_test)
y_pred

from sklearn.metrics import accuracy_score
from sklearn import metrics

metrics.accuracy_score(y_test,y_pred)

from sklearn.metrics import confusion_matrix
mat = confusion_matrix(y_test, y_pred)
mat

"""2. KNN Algorithm"""

import numpy as np
import pandas as pd

from sklearn.neighbors import KNeighborsClassifier

knn=KNeighborsClassifier(n_neighbors=2,metric='euclidean',p=2)
knn.fit(X_train,y_train)

y_pred=knn.predict(X_test)
y_pred

from sklearn.metrics import accuracy_score

score=accuracy_score(y_test,y_pred)
score

from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns
mat = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(15,8))
sns.heatmap(mat,annot=True,square=True,cmap='RdPu')
plt.ylabel('Actual Label')
plt.xlabel('Predicted Label')
title='Accuracy Score: {0}'.format(score)
plt.title(title,size=12)

#For selecting K value
error_rate = []

# Will take some time
for i in range(1,40):

    knn = KNeighborsClassifier(n_neighbors=i)
    knn.fit(X_train,y_train)
    pred_i = knn.predict(X_test)
    error_rate.append(np.mean(pred_i != y_test))

import matplotlib.pyplot as plt
plt.figure(figsize=(10,6))
plt.plot(range(1,40),error_rate,color='blue', linestyle='dashed', marker='o',
         markerfacecolor='red', markersize=10)
plt.title('Error Rate vs. K Value by Elbow Method')
plt.xlabel('K')
plt.ylabel('Error Rate')

"""3. Random Forest Algorithm"""

from sklearn.ensemble import RandomForestClassifier

rfc=RandomForestClassifier(n_estimators=250,random_state=100)
rfc.fit(X_train,y_train)

y_pred=rfc.predict(X_test)
y_pred

metrics.accuracy_score(y_test,y_pred)

from sklearn.metrics import confusion_matrix
mat = confusion_matrix(y_test, y_pred)

from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns
mat = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(15,8))
sns.heatmap(mat,annot=True,square=True,cmap='RdPu')
plt.ylabel('Actual Label')
plt.xlabel('Predicted Label')
title='Accuracy Score: {0}'.format(score)
plt.title(title,size=12)

"""4. Support vector machine Algorithm"""

from sklearn import svm
from sklearn.svm import SVC

sc=SVC(C=100,gamma=0.001)
sc.fit(X_train,y_train)

pred=sc.predict(X_test)
pred

Score=sc.score(X_test,y_test)

mat_s = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(15,8))
sns.heatmap(mat,annot=True,square=True,cmap='RdPu')
plt.ylabel('Actual Label')
plt.xlabel('Predicted Label')
title='Accuracy Score: {0}'.format(Score)
plt.title(title,size=12)
