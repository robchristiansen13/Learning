import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader as web

#pick any date after January of 2010
#let's pretend that you had $1000 dollars to invest at that date
#how much would it be today if you have invested back then and sold in on 1st of April 2019
#remotely download the SPX index from your date to 1st of April 2019
#load the FTSE from the file, and select values from your date  to 1st of April 2019
#normalize the return of each index for "Close" column so you can calculate your total return at any given date
#"invest" $1000 dollars on your date and make sure that you show your total gain/loss at every date
#plot both "investments" in SPX and FTSE on the same graph with names of "US Returns" and "EUR Returns" respectively.

fromDate = "2010-09-01"
toDate = "2019-04-01"
initialInvestment = 1000
productList = ['SPY', 'VGK'] #The list of desired products are listed here. The VGK is Vanguard FTSE Europe ETF that tracks the FTSE

# Getting all weekdays between fromDate and toDate
all_weekdays = pd.date_range(start=fromDate, end=toDate, freq='B', normalize=True)
# print(all_weekdays)

# Additional tutorial: https://www.learndatasci.com/tutorials/python-finance-part-yahoo-finance-api-pandas-matplotlib/

dict_of_df = {} # Create a dictionary of dataframes because it's bad form to create dynamically named dataframes

                # Example: https://stackoverflow.com/questions/40973687/create-new-dataframe-in-pandas-with-dynamic-names-also-add-new-column
for product in productList:
    df_name = 'dfData_' + str(product) # This will name the dataframe dataframe. Useful for later when required to join multiple frames together
    dict_of_df[df_name] = web.DataReader(product,"yahoo",fromDate,toDate)

    # Getting just the adjusted closing prices. This will return a Pandas DataFrame
    # The index in this DataFrame is the major index of the panel_data.
    dict_of_df[df_name].rename_axis('Date')

    # How do we align the existing prices in adj_close with our new set of dates?
    # All we need to do is reindex close using all_weekdays as the new index
    dict_of_df[df_name] = dict_of_df[df_name].reindex(all_weekdays)
    dict_of_df[df_name] = dict_of_df[df_name].fillna(method='ffill')

    # Get the first adj close value to use in the normalization
    #print(dfData['Adj Close'][0]) # Get the first adj close value to use in the normalization
    baseline_adj_close = dict_of_df[df_name]['Adj Close'][0]

    dict_of_df[df_name][str(product) + "_returns"] = dict_of_df[df_name]['Adj Close'] / baseline_adj_close
    dict_of_df[df_name][str(product) + "_investment_value"] = dict_of_df[df_name][str(product) + "_returns"] * initialInvestment

dfJoinedData = pd.DataFrame()
dfLoop = pd.DataFrame()
counter = 0

for dfLoop in dict_of_df:
    # Having retrieved all the data for the desired products, we can now merge the dataframes together
    # The first time through the loop set dfJoinedData to the first dataframe
    if counter == 0:
        dfJoinedData = dict_of_df[dfLoop]
    else:
        dfJoinedData = pd.merge(dfJoinedData, dict_of_df[dfLoop], how="inner", left_index=True, right_index=True)
    counter = counter + 1

print(dfJoinedData)

# We now have a dataframe, df_joined, with all the data combined

# gca stands for 'get current axis' to combine the series into one graph
ax = plt.gca()
ax.set(xlabel=str(fromDate) + ' to ' + str(toDate), ylabel="Dollars")

dfJoinedData.plot(title='Amount of $' + str(initialInvestment) + " Invested Over Time",
                  kind='line', y='SPY_investment_value', label='US Returns', color='blue', ax=ax)
dfJoinedData.plot(kind='line', y='VGK_investment_value', label='EUR Returns', color='red', ax=ax)

plt.show()
plt.savefig('outputfile.png')

