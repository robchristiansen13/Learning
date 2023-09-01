# You work at a low latency trading firm and are asked to deliver the order book data provided in order_book_data.txt to a superior
# The problem is that the data isn't formatted correctly. Please complete the following steps to apropriately format the data
# Notice, the first column is a ticker, the second column is a date, the third column is a Bid, the fourth column is an Ask, and the fifth column is a currency type
# 1. Open order_book_data.txt
# 2. Remove the order book lines. i.e. ***** Order Book: ###### *****
# 3. Get rid empty lines
# 4. Get rid of spaces
# 5. Notice that there are two currencies in the order book; USD and YEN. Please convert both the Bid and Ask price to USD (if not already)
# The Bid and Ask are the 3rd and 4th column, respectively
# 6. Create a header line Ticker, Date, Bid, Ask
# 7. Save the header line and properly formatted lines to a comma seperated value file called mktDataFormat.csv

import csv
usdyen = 134.21 # Set the exchange rate
header = ['Ticker', 'Date', 'Bid', 'Ask']

inputf = open('order_book_data.txt', 'r') # Open in read mode
outputf = open('mktDataFormat.csv', 'w') # Open in write mode
writer = csv.writer(outputf)
writer.writerow(header)

counter = 0
cleanArray = [] # myArray will hold the cleaned up values
for line in inputf:
    if line[0:2] == '\n': continue # This removes the empty lines
    if '*' in line: continue # This removes the *** lines
    line = line.replace('\t', '') # This replaces any tabs
    line = line.replace(' , ', ',') # This replaces the spaces around the commas
    # print(f'line {counter}: {line}')
    cleanArray.append(line)

#print (cleanArray)
csv_object = csv.reader(cleanArray)

for line in csv_object:
    if line[4] == 'YEN':
        line[2] = float(line[2]) / usdyen
        line[3] = float(line[3]) / usdyen
        line[4] = 'USD'
    writer.writerow(line)

inputf.close()
outputf.close()



