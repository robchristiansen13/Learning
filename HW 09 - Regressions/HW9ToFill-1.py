
from datetime import datetime
from sklearn import linear_model
from sklearn.metrics import r2_score
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

#Through this exercise we will answer the question does difference in rates affects the FX rates


import pandas_datareader as web
import pandas

fromDate = "2010-01-01"
toDate = datetime.today()

#Download "U.S. / Euro Foreign Exchange Rate" from Jan 1 2010 to today from FRED
dfFX = web.DataReader('DEXUSEU',"fred",fromDate,toDate)
dfFX = dfFX.dropna() # This will remove the NaN that come back from Fred

#Download "Overnight London Interbank Offered Rate (LIBOR), based on Euro  " from Jan 1 2010 to today from FRED
dfEU = web.DataReader('IRSTCI01EZM156N',"fred",fromDate,toDate)
dfEZ = dfEU.dropna() # This will remove the NaN that come back from Fred

#Download "Overnight London Interbank Offered Rate (LIBOR), based on U.S. Dollar " from Jan 1 2010 to today from FRED
dfUS = web.DataReader('IRSTCI01USM156N',"fred",fromDate,toDate)
dfUS = dfUS.dropna() # This will remove the NaN that come back from Fred

#Bring them all together for common dates - requires two joins because there are three tables
dfJoinedData = pandas.merge(dfFX, dfEU, how="inner", left_on='DATE', right_on='DATE') # Join dfFX & dfEU
dfJoinedData = pandas.merge(dfJoinedData, dfUS, how="inner", left_on='DATE', right_on='DATE') # Add in dfUS

#Calculate the ABSOLUTE difference between EUR and USD rates into a new column called Rate Diff
dfJoinedData["Rate Diff"] = dfJoinedData["IRSTCI01EZM156N"] - dfJoinedData["IRSTCI01USM156N"]

#Calculate the per cent change for EUR FX rate and difference between USD & EUR rates
dfPctChange = dfJoinedData.pct_change() # Handy function!
dfJoinedData = pandas.merge(dfJoinedData, dfPctChange, how="inner", left_on='DATE', right_on='DATE') # Join in pct_change data

# Drop the columns where we don't care about the rate change
dfJoinedData = dfJoinedData.drop(["IRSTCI01EZM156N_y", "IRSTCI01USM156N_y"],axis=1)

# Rename the columns to the desired names
dfJoinedData = dfJoinedData.rename(columns={
    "DEXUSEU_x":"DEXUSEU",
    "IRSTCI01EZM156N_x":"IRSTCI01EZM156N",
    "IRSTCI01USM156N_x":"IRSTCI01USM156N",
    "Rate Diff_x":"Rate Diff",
    "Rate Diff_y":"Rate Diff Pct",
    "DEXUSEU_y":"FX Rate Pct"
})

dfJoinedData = dfJoinedData.drop(index=dfJoinedData.index[0], axis=0) # Drop the first row because the rate of changes are NaN
#print(dfJoinedData)
dfJoinedData.to_excel("HW9_final_data.xlsx", index=False) # Don't include the index


#Regress whether change in difference in USD & EUR rates has effect on EUR FX rate
# Independent Variable (x): Pct Difference in Rates
# Dependent Variable (y): Pct Different in FX rates

# Need to extract desired dataframe columns to NumPy arrays to feed the linear algorithm function
Xtrain = dfJoinedData["Rate Diff Pct"].to_numpy()
Ytrain = dfJoinedData["FX Rate Pct"].to_numpy()

# LinearRegression() expects 2 dimension arrays, currently 1 dimension array instead
Xtrain = Xtrain.reshape(-1,1)
Ytrain = Ytrain.reshape(-1,1)


# Apply linear regression
linRegr = linear_model.LinearRegression()
linRegr.fit(Xtrain,Ytrain)
YpredSK = linRegr.predict(Xtrain)

#Check your r2 score
r2easy =r2_score(Ytrain,YpredSK)

print("Our calculated coeffs m:{} and b:{} and our r2 is {}".format(linRegr.coef_, linRegr.intercept_,r2easy))

#Answer the question -- does change in rates affect the change in FX rates?

plt.scatter(Xtrain, Ytrain)
#plt.scatter(Xs, Yreal)
plt.show()




