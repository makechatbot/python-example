
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.datasets import load_iris

iris = load_iris()
X, y = iris.data, iris.target

# iris_df = pd.DataFrame(X, columns=list(iris.feature_names))
# print(iris_df.describe())
# iris_df.boxplot()
# iris_df.plot()
# plt.show()


y1 = np.vstack(y)
iris_df = pd.DataFrame(np.hstack((X, y1)), columns=iris.feature_names+['target'])
iris_df.corr()


from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import Pipeline
from sklearn.cross_validation import KFold
from sklearn.grid_search import GridSearchCV

iris = datasets.load_iris()
X, y = iris.data, iris.target  # 0.953
# X = iris_df.iloc[:, [0,1]] # 0.733
# X = iris_df.iloc[:, [2,3]] # 0.947
kf = KFold(len(y), n_folds=10)

## KNN
estimators = [('knn', KNeighborsClassifier())]
parameters = {'knn__n_neighbors':(7,), 'knn__weights':('distance',)}

pipeline = Pipeline(estimators)
grid_search = GridSearchCV(pipeline, parameters, n_jobs=-1, verbose=1, cv=kf)
grid_search.fit(X, y)
print("Best score: %0.3f" % grid_search.best_score_)

