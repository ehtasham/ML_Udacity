#GaussianNB Deployment on Terrain Data
from sklearn.naive_bayes import GaussianNB
clf=GaussianNB()
clf.fit(features_train, labels_train)
return clf
    