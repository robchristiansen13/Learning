from datetime import datetime
import pandas_datareader as web
import pandas


fromDate = "2014-02-01"
toDate = "2016-02-01"
productList = ['DGS6MO', 'DGS1', 'DGS5', 'DGS10'] #The list of desired maturities can be added here
dfToExcel = pandas.DataFrame()
rowCollector = []

# The fred import from the Federal Reserve is natively supported in pandas
for product in productList:
    dfData = web.DataReader(product,"fred",fromDate,toDate)
    dfData.set_axis(['value'], axis=1, inplace=True)
    dfData = dfData.dropna() # This will remove the NaN that come back from Fred
    dfData["product"] = product
    dfData = dfData.reset_index() # This moves the index to be used as a colum
    print(dfData)


    dfDataStats = pandas.DataFrame() # Define an empty dataframe to store the summary stats
    dfDataStats["product"] = product
    dfDataStats["average"] = dfData.mean()
    dfDataStats["std_dev"] = dfData.std()
    dfDataStats["min_value"] = dfDataStats.apply(lambda row: row.average - row.std_dev, axis=1) #axis 1 applys to column lambda creates math problem
    dfDataStats["max_value"] = dfDataStats.apply(lambda row: row.average + row.std_dev, axis=1)
    dfDataStats["product"] = dfDataStats["product"].fillna(product)
    print(dfDataStats)

    #Now we need to join dfData with the summary data in dfDataStats
    dfJoinedData = pandas.merge(dfData, dfDataStats, how="inner", left_on='product', right_on='product')
    print(dfJoinedData)
    dfFiltered = dfJoinedData.where((dfJoinedData['value'] < dfJoinedData["min_value"]) | (dfJoinedData['value'] > dfJoinedData["max_value"]))
    dfFiltered = dfFiltered[dfFiltered['value'].notna()] # This removes the NaN rows in the [product] column
    #dfFiltered = dfFiltered.drop(product,1) # Drop the column where the maturity is the column header
    rowCollector.append(dfFiltered)
    #dfToExcel = dfToExcel.concat(dfFiltered)
    print("Product: " + product)
    print(dfFiltered)

rowCollector = pandas.concat(rowCollector)
print(rowCollector)

rowCollector = rowCollector.dropna()
rowCollector = rowCollector.drop('average', 1)
rowCollector = rowCollector.drop('std_dev', 1)
rowCollector = rowCollector.drop('min_value', 1)
rowCollector = rowCollector.drop('max_value', 1)
rowCollector.to_excel("sigma.xlsx", index=False) # Don't include the index  

#rowCollector = rowCollector.drop("average,1)

# df_join = pandas.merge(dfDataAvg,dfDataStd, left_index=True, right_index=True)
# df_join["product"] = df_join.apply(lambda row: product)

# df_filtered = pandas.merge(dfData, df_join, how="outer")
#
# oneYear = web.DataReader("DGS1","fred",fromDate,toDate)
# oneYearAverage = oneYear.mean()
# oneYearAverage.name = "mean"
#
#
# fiveYear = web.DataReader("DGS5","fred",fromDate,toDate)
# fiveYearAverage = fiveYear.mean()
# fiveYearAverage.name = "mean"
#
# tenYear = web.DataReader("DGS10","fred",fromDate,toDate)
# tenYearAverage = tenYear.mean()
# tenYearAverage.name = "mean"
# #print(tenYearAverage)
# #print(fiveYearAverage)
# #print(oneYearAverage)
# #print(sixMonthAverage)
# #dfInflation = web.DataReader("CPIAUCSL","fred",fromDate,toDate)
# #print(dfInflation.head(20))
#
# # df = web.DataReader(ticker,'yahoo',fromDate,toDate)
# # df = df[["Close"]]
# #df.to_csv("test.csv")
# # print(df.tail())
#
# # dfRu = web.DataReader("MGNT",'moex',fromDate,toDate)
# # dfRu.to_csv("rus.csv")
# # dfRu = dfRu[dfRu["BOARDID"]== "TQBR"]
# # dfRu = dfRu[["CLOSE"]]
# # dfRu["CLOSE"] = dfRu["CLOSE"]/60
# # print(dfRu)
#
# # dfJoin = df.join(dfRu,how="inner")
# # print(dfJoin)
#
