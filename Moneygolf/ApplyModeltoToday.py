import pandas as pd
import numpy as np

def mapRecruitingRegion(x):
    if x in ["ID","MT","NM","UT","WY","I"]: # Most 'recruitable' at University of Utah
        return 1
    if x in ["AB",'AZ',"BC","CO","NV"]:
        return 2
    if x in ['CA','HI','OR','WA']:
        return 3
    if x in ['IL','IN','KS','SD','TX']:
        return 4
    if x in ['AL','AR','CT','DC','DE','FL','GA','IA','KY','LA','MA','MD','ME','MI','MN','MO','MS','NC','NE','NH','NJ','NY',
        'OH','OK','ON','PA','QC','RI','SC','TN','VA','VT','WI','WV']:
        return 5
    else:
        return 6 # Least 'recruitable' at University of Utah
    return x

def applyModel(coef1, value1, coef2, value2, y_intercept):
    return (coef1 * value1) + (coef2 + value2) + y_intercept

# Steps to clean data from https://rankings.golfweek.com/rankings/default.asp?T=boys
# a) Remove the default '50' from the results per page
# b) Paste into Excel
# c) Add two columns right of "Sked (Rank)"
# d) Use Excel's text-to-columns function to break the column on a fixed width so that the Sked and Sked(Rank) and separated
# e) The only columns we care about are: Rank   Name	Grad Year	State	Rating  Sked
# Highlight from "Rank"

dfJuniorGolfers=pd.read_excel('DataClean/CurrentJuniorGolfers.xlsx', usecols=['Rank','Name','Grad Year','State','Rating','Sked (Rank)'])
dfJuniorGolfers = dfJuniorGolfers.dropna() # Drop empty lines

dfJuniorGolfers['Sked'] = dfJuniorGolfers['Sked (Rank)'].str.strip() # Remove leading and trailing spaces just in case
dfJuniorGolfers['Sked'] = dfJuniorGolfers['Sked (Rank)'].str[0:5] # We're only interested in the first 5 characters
dfJuniorGolfers['Sked'] = pd.to_numeric(dfJuniorGolfers['Sked'])
dfJuniorGolfers['Grad Year'] = pd.to_numeric(dfJuniorGolfers['Grad Year'], downcast="integer") # By default to_numeric returns a float. Downcast returns an integer

# Append data
#   Append a column representing how "recruitable" the state for the program
dfJuniorGolfers['Recruiting_Region'] = dfJuniorGolfers.apply(lambda row: mapRecruitingRegion(row['State']), axis=1)

# BIN the Rating and Schedule into Deciles
numBins = 10
decileLabelsLowValueGood=['9', '8', '7', '6', '5', '4', '3', '2', '1', '0']
dfJuniorGolfers['bin_rating_HS'] = pd.to_numeric(pd.qcut(dfJuniorGolfers['Rating'], numBins, duplicates='drop', labels=decileLabelsLowValueGood))
dfJuniorGolfers['bin_Sked'] = pd.to_numeric(pd.qcut(dfJuniorGolfers['Sked'], numBins, duplicates='drop', labels=decileLabelsLowValueGood))
dfJuniorGolfers['bin_rating_HS'] = (dfJuniorGolfers['bin_rating_HS'])


# Retrieve the previously calculated model
dfModelImport = pd.read_excel('DataOutputs/e_modelOutput.xlsx')
# print(dfModelImport)

model_bin_rating_HS = pd.to_numeric(dfModelImport["bin_rating_HS"][0])
model_bin_Sked = pd.to_numeric(dfModelImport["bin_Sked"][0])
model_Y_Intercept = pd.to_numeric(dfModelImport["Y_Intercept"][0])

print(model_bin_rating_HS)
print(model_bin_Sked)
print(model_Y_Intercept)

dfJuniorGolfers['ModelOutput'] = dfJuniorGolfers.apply(lambda row: (applyModel(model_bin_rating_HS, row['bin_rating_HS'], model_bin_Sked, row['bin_Sked'], model_Y_Intercept)), axis=1)

decileLabelsHighValueGood=['0','1','2','3','4','5','6','7','8','9']
dfJuniorGolfers['bin_ModelOutput'] = pd.to_numeric(pd.qcut(dfJuniorGolfers['ModelOutput'], numBins, duplicates='drop', labels=decileLabelsHighValueGood))
dfJuniorGolfers.sort_values(by=['ModelOutput','bin_ModelOutput','Recruiting_Region'], ascending=[False,False,True], inplace=True)

dropUnneccesaryColumns = ['Sked (Rank)']
dfJuniorGolfers = dfJuniorGolfers.drop(dropUnneccesaryColumns, axis=1)  # Populate with columns to remove


dfJuniorGolfers.to_excel('DataOutputs/f_CurrentJuniorGolfers.xlsx', index=False)
print(dfJuniorGolfers.head(50))




