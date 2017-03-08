
# 붓꽃 데이터로 학습한 kNN 모델 평가

import numpy as np
from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier

# load data
iris = datasets.load_iris()
X, y = iris.data, iris.target

knn = KNeighborsClassifier(n_neighbors=2)
knn.fit(X, y)
print(knn.score(X, y)) # 결과 0.98



# DummyClassifier 모델의 평가

from sklearn.dummy import DummyClassifier
dummy = DummyClassifier(strategy='stratified',random_state=0)
#다른 매개 변수 stratified, most_frequent
dummy.fit(X, y)
print(dummy.score(X, y)) # 결과 0.36


from sklearn.metrics import accuracy_score
knn.fit(X, y)
print(accuracy_score(knn.predict(X), y)) # 결과 0.98

