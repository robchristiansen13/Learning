import pandas as pd
import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt
import openpyxl

import WOE as woe
from WOE import data_vars
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, roc_curve, roc_auc_score
from sklearn.metrics import classification_report
import sklearn.metrics


def mapTypeOfEmployment(x):
    if "Government" in x:
        return "1"
    if "Self-Employed" in x:
        return "2"
    if "Self-Private" in x:
        return "3"
    return x

#reduce Marital Status to four  categories -- Married, Separated, Never Married, Widowed
def mapMaritalStatus(x):
    if("Divorced" in x):
        return "Separated"
    if("Separated" in x):
        return "Separated"
    if("Never-married" in x):
        return "Never Married"
    if("Married" in x):
        return "Married"
    if("Widowed" in x):
        return "Widowed"
    return x

def mapNativeCountry(x):
    if "United-States" in x:
        return "United States"
    else:
        return "Not United States"
    return x

def correl(X_train):
    cor = X_train.corr()
    corrm = np.corrcoef(X_train.transpose())
    # corr = corrm - np.diagflat(corrm.diagonal())
    # print("max corr:",corr.max(), ", min corr: ", corr.min())
    # c1 = cor.stack().sort_values(ascending=False).drop_duplicates()
    # high_cor = c1[c1.values!=1]
    # ## change this value to get more correlation results
    # thresh = 0.9
    # display(high_cor[high_cor>thresh])

def printOutTheCoefficients(params,coeffecients,intercept):
    tParams = params[np.newaxis].T
    tCoeffs = coeffecients.T
    total = np.concatenate([tParams,tCoeffs],axis=1)
    totalDF = pd.DataFrame(data=total)
    totalDF.to_excel("modelOutput.xlsx")
    print(totalDF)

#load the data from the dataset
df = pd.read_csv ('adultIncome_proc.csv', skipinitialspace=True)
df['Martial-status'] = df.apply(lambda row: mapMaritalStatus(row['Martial-status']), axis=1)

#drop obviously correlated values
# ANSWER: No correlation at this point
dropColsHighCorrelated = []
df = df.drop(dropColsHighCorrelated, axis=1)  # Populate with columns to remove
correlation = df.corr()
print(correlation.head()) # Really cool function that correlates everything against itself
#correlation.to_excel('correlation.xlsx') #Columns that have correlation greater than 0.5 are highly correlated and can be removed
#sb.heatmap(correlation) # HEAT MAP! Wow!
#plt.show()

#map countries to born in United States or not
df['Native Country'] = df.apply(lambda row: mapNativeCountry(row['Native Country']), axis=1)
# print(df['Native Country'])

#determine if any fields are correlated with each other
dropColsHighCorrelated = []
df = df.drop(dropColsHighCorrelated, axis=1)  # Populate with columns to remove
correlation = df.corr()
print(correlation.head()) # Really cool function that correlates everything against itself
#correlation.to_excel('correlation.xlsx') #Columns that have correlation greater than 0.5 are highly correlated and can be removed
sb.heatmap(correlation) # HEAT MAP! Wow!
#plt.show()

#find statistically significant or unreasonable variables using WOE file (Weight of Evidence)

finalIV,IV = woe.data_vars(df,df["income-80k+"])
IV.to_excel("IVOutput.xlsx")

# These are the parameters between 0.03 and 1
columnWIV = ['Degree',
             'occupation',
             'Years of education[=
             'age',
             'Sex',
             'hours-worked',
             'type-of-employment',
             'Race',
             'income-80k+']

df = pd.read_csv ('adultIncome_proc.csv', skipinitialspace=True, usecols=columnWIV)
#print(df.head())
df.to_csv("checkSelectedData.csv")

#if there are missing values, fill it with the worst value possible
#df["XXX'] = df["XXX'].fillna(100) #Conservative value

#dummy encode all of the non-quantitative values

employmentType = pd.get_dummies(df["type-of-employment"]) #Encodes every value as a true or false
occupationType = pd.get_dummies(df["occupation"]) #Encodes every value as a true or false
degreeType = pd.get_dummies(df["Degree"]) #Encodes every value as a true or false
raceType = pd.get_dummies(df["Race"]) #Encodes every value as a true or false
sexType = pd.get_dummies(df["Sex"]) #Encodes every value as a true or false

# print(employmentType.head())

#drop dummyfied variables
df = df.drop(["type-of-employment", 'occupation', 'Degree', 'Race', 'Sex'], axis=1)
#print(df)

# print(dfReady)

#create table with base quantitative values and with dummy values
dfReady = pd.concat([df,employmentType],axis=1) #The first time join with df, all other times use dfReady
dfReady = pd.concat([dfReady,occupationType],axis=1)
dfReady = pd.concat([dfReady,degreeType],axis=1)
dfReady = pd.concat([dfReady,raceType],axis=1)
dfReady = pd.concat([dfReady,sexType],axis=1)
print(dfReady)

#separate for results and input sets

dfInputs = dfReady.drop('income-80k+', axis=1) # The input variables
dfResults = dfReady['income-80k+'] #The outcome variable

#split between sets

#run logistic regresstion
inputsTrain, inputsTest, resultTrain, resultTest = train_test_split(dfInputs, dfResults, test_size=0.3, random_state=1)
#test_size of 30% - therefore the train set will be the remaining will be 70%
LogReg = LogisticRegression()
LogReg.fit(inputsTrain, resultTrain)

#print classification report
print("Coefs(Mns) aka slopes:", LogReg.coef_)
print("Y Intercept(b):", LogReg.intercept_)

#print resuls using printOutCoefficients method to excel and run 5 different rows through the model in excel
printOutTheCoefficients(dfInputs.columns.values, LogReg.coef_, LogReg.intercept_)