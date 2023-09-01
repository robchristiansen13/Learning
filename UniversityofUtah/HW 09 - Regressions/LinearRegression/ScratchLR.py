from  mysteryFunctions import *
import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model
from sklearn.metrics import r2_score

def plotTheLine(inputParams,m,b):
    result = []
    for x in inputParams:
        y = m*x + b
        result.append(y)

    return result

Xs = list(range(-20,20))
Ycalc = plotTheLine(Xs,2,3)

Yreal = mysteryFunctionLarge(Xs)

Xactual = np.array(Xs)
Yactual = np.array(Yreal)

denominator = Xactual.dot(Xactual) - Xactual.mean()*Xactual.sum()
m = ( Xactual.dot(Yactual)-Yactual.mean()*Xactual.sum())/denominator
b = ( Yactual.mean()*Xactual.dot(Xactual)-Xactual.dot(Yactual)*Xactual.mean())/denominator

Ypredicted = plotTheLine(Xs,m,b)

Ypredicted = np.array(Ypredicted)

predDiff = Yactual - Ypredicted
avgDiff = Yactual - Ypredicted.mean()
r2 = 1 - (predDiff.dot(predDiff)/avgDiff.dot(avgDiff))

print("Our calculated coeffs m: {} and b: {} and our r2 is {}".format(m,b,r2))

linRegr = linear_model.LinearRegression()

Xtrain = Xactual.reshape(len(Xactual),1)
Ytrain = Yactual.reshape(len(Yactual),1)

linRegr.fit(Xtrain,Ytrain)
YpredSK = linRegr.predict(Xtrain)

r2easy =r2_score(Ytrain,YpredSK)

print("Our calculated coeffs m:{} and b:{} and our r2 is {}".format(linRegr.coef_, linRegr.intercept_,r2easy))

plt.plot(Xs, Ycalc, "r--")
plt.plot(Xs,Ypredicted,"g")
plt.scatter(Xs, Yreal)
plt.show()