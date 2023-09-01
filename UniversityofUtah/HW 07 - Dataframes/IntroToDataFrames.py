
#Step 1(10 points): Remotely Download "Treasury Constant Maturity Rate" from FRED
#(https://fred.stlouisfed.org/categories/115) from 02/01/2014 to 02/01/2016:
#6-Month
#1-Year
#5-Year
#10-Year
#Step 2( 5 points ): Determine the average and standard deviation for each of the maturities( maturity is 6-month, 1 year, etc.)
#Step 3( 5 points ): Select only those rows that have value more or less than avg +/- 1 std
#Step 4( 10 points ): Create a dataframe which has only those rows for which all of the maturities
#has value outside of avg +/- 1 std. Hint: think about joins for frames in step 3
#Step 5( 5 points): Save the generated dataframe as sigma.xlsx
#Please upload this filled file and sigma.xlsx


# Helpful tutorial: https://simplernerd.com/python-pandas-read-csv-from-url/

# Start by filtering by month: https://fred.stlouisfed.org/categories/115?t=monthly&ob=pv&od=desc
# Add to graph: https://fred.stlouisfed.org/graph/?id=GS10,GS6M,GS1,GS5,
# Filter the dates and copy the CSV link: https://fred.stlouisfed.org/graph/fredgraph.csv?bgcolor=%23e1e9f0&chart_type=line&drp=0&fo=open%20sans&graph_bgcolor=%23ffffff&height=450&mode=fred&recession_bars=on&txtcolor=%23444444&ts=12&tts=12&width=1168&nt=0&thu=0&trc=0&show_legend=yes&show_axis_titles=yes&show_tooltip=yes&id=GS10,GS6M,GS1,GS5&scale=left,left,left,left&cosd=2014-02-01,2014-02-01,2014-02-01,2014-02-01&coed=2016-02-01,2016-02-01,2016-02-01,2016-02-01&line_color=%234572a7,%23aa4643,%2389a54e,%2380699b&link_values=false,false,false,false&line_style=solid,solid,solid,solid&mark_type=none,none,none,none&mw=3,3,3,3&lw=2,2,2,2&ost=-99999,-99999,-99999,-99999&oet=99999,99999,99999,99999&mma=0,0,0,0&fml=a,a,a,a&fq=Monthly,Monthly,Monthly,Monthly&fam=avg,avg,avg,avg&fgst=lin,lin,lin,lin&fgsnd=2020-02-01,2020-02-01,2020-02-01,2020-02-01&line_index=1,2,3,4&transformation=lin,lin,lin,lin&vintage_date=2022-06-20,2022-06-20,2022-06-20,2022-06-20&revision_date=2022-06-20,2022-06-20,2022-06-20,2022-06-20&nd=1953-04-01,1981-09-01,1953-04-01,1953-04-01
# Copy link to data: https://fred.stlouisfed.org/graph/fredgraph.csv?bgcolor=%23e1e9f0&chart_type=line&drp=0&fo=open%20sans&graph_bgcolor=%23ffffff&height=450&mode=fred&recession_bars=on&txtcolor=%23444444&ts=12&tts=12&width=1168&nt=0&thu=0&trc=0&show_legend=yes&show_axis_titles=yes&show_tooltip=yes&id=GS10,GS6M,GS1,GS5&scale=left,left,left,left&cosd=1953-04-01,1981-09-01,1953-04-01,1953-04-01&coed=2022-05-01,2022-05-01,2022-05-01,2022-05-01&line_color=%234572a7,%23aa4643,%2389a54e,%2380699b&link_values=false,false,false,false&line_style=solid,solid,solid,solid&mark_type=none,none,none,none&mw=3,3,3,3&lw=2,2,2,2&ost=-99999,-99999,-99999,-99999&oet=99999,99999,99999,99999&mma=0,0,0,0&fml=a,a,a,a&fq=Monthly,Monthly,Monthly,Monthly&fam=avg,avg,avg,avg&fgst=lin,lin,lin,lin&fgsnd=2020-02-01,2020-02-01,2020-02-01,2020-02-01&line_index=1,2,3,4&transformation=lin,lin,lin,lin&vintage_date=2022-06-20,2022-06-20,2022-06-20,2022-06-20&revision_date=2022-06-20,2022-06-20,2022-06-20,2022-06-20&nd=1953-04-01,1981-09-01,1953-04-01,1953-04-01

# In PyCharm, go to View > Tool Windows > Python Packages and install pandas and "requests"
import pandas as wb
import datetime as date
import requests

URL = "https://fred.stlouisfed.org/graph/fredgraph.csv?bgcolor=%23e1e9f0&chart_type=line&drp=0&fo=open%20sans&graph_bgcolor=%23ffffff&height=450&mode=fred&recession_bars=on&txtcolor=%23444444&ts=12&tts=12&width=1168&nt=0&thu=0&trc=0&show_legend=yes&show_axis_titles=yes&show_tooltip=yes&id=GS10,GS6M,GS1,GS5&scale=left,left,left,left&cosd=2014-01-02,2014-01-02,2014-01-02,2014-01-02&coed=2016-02-01,2016-02-01,2016-02-01,2016-02-01&line_color=%234572a7,%23aa4643,%2389a54e,%2380699b&link_values=false,false,false,false&line_style=solid,solid,solid,solid&mark_type=none,none,none,none&mw=3,3,3,3&lw=2,2,2,2&ost=-99999,-99999,-99999,-99999&oet=99999,99999,99999,99999&mma=0,0,0,0&fml=a,a,a,a&fq=Monthly,Monthly,Monthly,Monthly&fam=eop,eop,eop,eop&fgst=lin,lin,lin,lin&fgsnd=2020-02-01,2020-02-01,2020-02-01,2020-02-01&line_index=1,2,3,4&transformation=lin,lin,lin,lin&vintage_date=2022-06-21,2022-06-21,2022-06-21,2022-06-21&revision_date=2022-06-21,2022-06-21,2022-06-21,2022-06-21&nd=1953-04-01,1981-09-01,1953-04-01,1953-04-01"
response = requests.get(URL)
open("fredgraph.csv", "wb").write(response.content)

# Read into a Pandas dataframe

# What we really need is a multi-index of both date and each maturity: https://stackoverflow.com/questions/16121392/how-to-read-csv-file-into-pandas-dataframe-with-multiple-row-index-level
df = wb.read_csv('fredgraph.csv', index_col=0)
print(df)
print()
# The following stack and reset the 20 rows x 5 columns dataframe into a dataframe with 100 rows
# Source: https://stackoverflow.com/questions/43874690/how-do-i-flatten-a-pandas-dataframe-keeping-index-and-column-names
df_stacked = df.stack().reset_index()
df_stacked.columns = ['DATE', 'PRODUCT', 'VALUE']
print(df_stacked)

df_stddev = df.std()
df_stddev.name = "std_dev"


df_avg = df.mean()
df_avg.name = "average"

# https://datacarpentry.org/python-socialsci/11-joins/index.html
df_joined = wb.merge(df_avg, df_stddev, left_index=True, right_index=True)

# Use a lambda function to add a column with simple math: https://towardsdatascience.com/create-new-column-based-on-other-columns-pandas-5586d87de73d
df_joined['min_value'] = df_joined.apply(lambda row: row.average - row.std_dev, axis=1)
df_joined['max_value'] = df_joined.apply(lambda row: row.average + row.std_dev, axis=1)
print(df_joined)
print()

# Join the df_stacked with the df_joined.
df_stacked = wb.merge(df_stacked, df_joined, left_on="PRODUCT", right_index=True, sort=True)
#print(df_stacked)
df_filtered = df_stacked.where((df_stacked["VALUE"] < df_stacked["min_value"]) | (df_stacked["VALUE"] > df_stacked["max_value"]))
# This returns a dataframe with many NaN rows. We can use dropna() to exclude them
df_filtered = df_filtered.dropna()
df_filtered = df_filtered.drop('average', 1)
df_filtered = df_filtered.drop('std_dev', 1)
df_filtered = df_filtered.drop('min_value', 1)
df_filtered = df_filtered.drop('max_value', 1)

df_filtered.to_excel("sigma.xlsx", index=False)
print(df_filtered)


