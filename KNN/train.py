import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from KNN import KNN

cmap = ListedColormap(['#FF0000','#00FF00'])

breast_cancer = datasets.load_breast_cancer() #dataset
#print(iris.data) feaures
#print(iris.target) labels
X, y = breast_cancer.data, breast_cancer.target
#print(iris.target[-30:]) just slicing
#done
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state = 1)
#print(X_train.shape) will tell row column  of trainiing data
#print(X_test.shape) will tell row coulmn of testing data
#print(y_train.shape) will tell rows label trained
#print(y_test.shape) will tell the rows label testing 
#test size ranges 0-1 keep increasing the size if you want to take more data for testing
#random-state is used to fix the spliting each time
#?
plt.figure()
plt.scatter(X[:,10],X[:,28], c=y, cmap=cmap, edgecolor='k')
plt.title("KNN Plot of breast_cancer")
plt.show()
#print(X[:,10])
#print(X[:,28])
#print(y.shape)

#done
clf = KNN(k=5) #top 5 least distance check
clf.fit(X_train, y_train) #settting features and labels
#print("testing : ",X_test) 
predictions = clf.predict(X_test) #test cases sending only with features ofcourse


#done
print("predictions : ",predictions)
print("actual result : ",y_test)
print("boolean check :",(predictions==y_test))
#print(np.sum(predictions==y_test)) same value(boolean) will count if same if ot the case then reduction occurs
#print(len(y_test)==len(predictions)) just checking length
acc = np.sum(predictions == y_test) / len(y_test)
print("accuray : ",acc*100)