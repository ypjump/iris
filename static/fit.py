__author__ = 'yp'
import json,pandas,seaborn,numpy
from sklearn import neighbors
from sklearn.preprocessing import LabelEncoder
def Fit():
    iris = pandas.read_csv(r"C:\Users\yp\PycharmProjects\iris\static\Iris2.csv")
    #在Python中 \ 是转义符，\u表示其后是UNICODE编码，因此\User在这里会报错，在字符串前面加个 r（rawstring  原生字符串），可以避免python与正则表达式语法的冲突！
    knn = neighbors.KNeighborsClassifier(7,weights='uniform')
    leb = LabelEncoder()#实例化一个label，用来将字符串类别变成sklearn能识别的类别
    leb.fit(iris["class"])
    features = ["sepal-length","sepal-width","petal-length","petal-width"]
    x = iris[features]
    y = leb.transform(iris["class"])
    model = knn.fit(x,y)
    return model,leb

