# This algorithm
import unicodecsv
import random
import operator
import math
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler


#1. Load the iris dataset and check shape of data and list of features ( X matrix)

df = pd.read_csv('Iris.txt', names=['sepal length','sepal width','petal length','petal width','target'])
print(df)

features = ['sepal length', 'sepal width', 'petal length', 'petal width']
# Separating out the features
x = df.loc[:, features].values
# Separating out the target
y = df.loc[:,['target']].values
# Standardizing the features
x = StandardScaler().fit_transform(x)

#2. By using sickit-learn, import and instantiate PCA with 2 components, then fit PCA to the iris dataset and transform it into 2 principal components.
pca = PCA(n_components=2)
principalComponents = pca.fit_transform(x)
principalDf = pd.DataFrame(data = principalComponents, columns = ['principal component 1', 'principal component 2'])

finalDf = pd.concat([principalDf, df[['target']]], axis = 1)

fig = plt.figure(figsize = (8,8))
ax = fig.add_subplot(1,1,1) 
ax.set_xlabel('Principal Component 1', fontsize = 15)
ax.set_ylabel('Principal Component 2', fontsize = 15)
ax.set_title('2 component PCA', fontsize = 20)
targets = ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']
colors = ['r', 'g', 'b']
for target, color in zip(targets,colors):
    indicesToKeep = finalDf['target'] == target
    ax.scatter(finalDf.loc[indicesToKeep, 'principal component 1']
               , finalDf.loc[indicesToKeep, 'principal component 2']
               , c = color
               , s = 50)
ax.legend(targets)
ax.grid()
#3Plot the projected principal components and try to understand the data.
plt.show()
#4. pca.components_ has the meaning of each principal component, essentially how it was
#derived. Checking shape tells us it has 2 rows, one for each principal component and 4
#columns, proportion of each of the 4 features #for each row.

print (pca.components_)
print (pca.components_.shape)

print ("Meaning of the 2 components:")
for component in pca.components_:
	print (" + ".join("%.2f x %s" % (value, name)
		for value, name in zip(component, features)))