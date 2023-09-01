import pandas as pd
import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt
import openpyxl

import WOE as woe
from WOE import data_vars
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

# from sklearn.metrics import confusion_matrix, roc_curve, roc_auc_score
# from sklearn.metrics import classification_report
# import sklearn.metrics

def winPercentage(win,loss,tie):
    if (win + loss + tie) > 0:
        return win / (win + loss + tie)
    else:
        return '0'

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

# Load the data from the dependent variables dataset
df = pd.read_csv ('DataClean/BoysJuniorsLearningData.csv', skipinitialspace=False)
# print(df.dtypes)

# Strip() leading and trailing spaces
df['Name'] = df['Name'].str.strip()

#   Calculate the winning percentages for each tier
df['WPTop25'] = df.apply(lambda row: winPercentage(int(row['Top25W']), int(row['Top25L']), int(row['Top25T'])), axis=1)
df['WPTop50'] = df.apply(lambda row: winPercentage(int(row['Top50W']), int(row['Top50L']), int(row['Top50T'])), axis=1)
df['WPTop100'] = df.apply(lambda row: winPercentage(int(row['Top100W']), int(row['Top100L']), int(row['Top100T'])), axis=1)
df['WPOverall'] = df.apply(lambda row: winPercentage(int(row['OverallW']), int(row['OverallL']), int(row['OverallT'])), axis=1)

# Drop unnecessary columns from input file for High School variables
dropUnneccesaryColumns = ['DataSet','GradYear','Rank','Rank-TooFewEvents','Events','Top25W','Top25L','Top25T','Top50W','Top50L','Top50T','Top100W','Top100L','Top100T','OverallW','OverallL','OverallT','Sked-Rank']
df = df.drop(dropUnneccesaryColumns, axis=1)  # Populate with columns to remove
df.query("Rating >= 60",inplace=True) # Eliminate dirty data that is less than 60

# Load the data from the outcomes dataset
df_outcomes = pd.read_csv ('DataClean/CollegeOutcomes.csv', skipinitialspace=False, usecols=['Name','Rating'])
df_outcomes['Name'] = df_outcomes['Name'].str.strip()
df_outcomes['Rating'] = df_outcomes['Rating'].str.strip()
df_outcomes["Rating"] = pd.to_numeric(df_outcomes["Rating"])
df_outcomes.query("Rating >= 60",inplace=True) # Eliminate dirty data that has a rating less than 60

# Join outcomes with the inputs to manage a single dataframe
dfJoinedData = pd.merge(df, df_outcomes, how="inner", left_on='Name', right_on='Name')
# print(dfJoinedData.head())
# Drop unnecessary columns from merged file
dropUnneccesaryColumns = ['Name','IsNotSenior','State']
dfJoinedData = dfJoinedData.drop(dropUnneccesaryColumns, axis=1)  # Populate with columns to remove

# Convert column data to floats
dfJoinedData["WPTop25"] = pd.to_numeric(dfJoinedData["WPTop25"])
dfJoinedData["WPTop50"] = pd.to_numeric(dfJoinedData["WPTop50"])
dfJoinedData["WPTop100"] = pd.to_numeric(dfJoinedData["WPTop100"])
dfJoinedData["WPOverall"] = pd.to_numeric(dfJoinedData["WPOverall"])

# Determine if any fields are correlated with each other
correlation = dfJoinedData.corr() # Function that correlates everything against itself
correlation.to_excel('DataOutputs/a_correlation.xlsx') #Columns that have correlation greater than 0.5 are highly correlated and can be removed
# sb.heatmap(correlation) # HEAT MAP! Wow!
# plt.show()

# Find statistically significant or unreasonable variables using WOE file (Weight of Evidence)
finalIV,IV = woe.data_vars(dfJoinedData,dfJoinedData["Rating_y"])
IV.to_excel("DataOutputs/b_IVOutput.xlsx")
print("IVOutput.xlsx saved")

# Bin Columns into Deciles
numBins = 10
decileLabelsLowValueGood=['9', '8', '7', '6', '5', '4', '3', '2', '1', '0']
dfJoinedData['bin_rating_HS'] = pd.qcut(dfJoinedData['Rating_x'], numBins, duplicates='drop', labels=decileLabelsLowValueGood)
dfJoinedData['bin_Sked'] = pd.qcut(dfJoinedData['Sked'], numBins, duplicates='drop', labels=decileLabelsLowValueGood)
dfJoinedData['bin_rating_College'] = pd.qcut(dfJoinedData['Rating_y'], numBins, duplicates='drop', labels=decileLabelsLowValueGood)

# Based on the Weight of Evidence and Correlation results, the Winning Percentage columns should be dropped
dfJoinedData.to_excel('DataOutputs/c_dfJoinedData_all.xlsx')
dropUnneccesaryColumns = ['Rating_x', 'Sked', 'Rating_y', 'WPTop25', 'WPTop50', 'WPTop100', 'WPOverall']
dfJoinedData = dfJoinedData.drop(dropUnneccesaryColumns, axis=1)  # Populate with columns to remove
# print(dfJoinedData.dtypes) # Print out the column datatypes
# dfJoinedData.drop_duplicates(keep=False, inplace=True) # Drop any duplicate rows in the dataframe and replace the dfJoinedData dataframe
dfJoinedData.to_excel('DataOutputs/c_dfJoinedData.xlsx')

# Separate for results and input sets

dfInputs = dfJoinedData.drop('bin_rating_College', axis=1) # The input variables - remove the dependent variable from the dataframe
dfResults = dfJoinedData['bin_rating_College'] #The outcome variable

dfInputs.to_excel('DataOutputs/d_dfInputs.xlsx')
dfResults.to_excel('DataOutputs/d_dfResults.xlsx')

inputsTrain, inputsTest, resultTrain, resultTest = train_test_split(dfInputs, dfResults, test_size=.8, random_state=1)
# print(inputsTrain)
# print(inputsTest)
LogReg = LogisticRegression(max_iter=1000)
LogReg.fit(inputsTrain, resultTrain)

#print classification report
print(dfInputs.columns.values)
print("Coefs(Mns) aka slopes:", LogReg.coef_[-1]) # Just print out the last row
print("Y Intercept(b):", LogReg.intercept_[-1]) # Just print out the last row

# Build file to export with model parameters
# a) Capture the coefficients in a dataframe
dfModelExport = pd.DataFrame(data=LogReg.coef_[-1:], columns=dfInputs.columns.values) # Only get the last row

# b) Capture the Y Intercepts in a dataframe
dsYIntercept = pd.Series(data=LogReg.intercept_[-1:]) # Only get the last row
dfYIntercept = pd.DataFrame(data=dsYIntercept, columns={'Y_Intercept'})

# c) Concatenate (aka append) the two dataframes into a single dataframe
dfModelExport = pd.concat([dfModelExport, dfYIntercept], axis=1) # Axis=1 means to append as a column (Axis=0 would add the dataframe as new rows)

# d) Save output to file
print(dfModelExport)
dfModelExport.to_excel('DataOutputs/e_modelOutput.xlsx')
