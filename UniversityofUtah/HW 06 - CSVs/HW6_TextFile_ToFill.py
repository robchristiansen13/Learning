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
# 7. Save the header line and propely formatted lines to a comma seperated value file called mktDataFormat.csv
usdyen = 134.21

file = open("orderbookData2.txt", "r")
lines = file.readlines()
file.close()

data = []
for line in lines:
    if "**" in line :continue
    if line[0:2] == "\n":continue
    line = line.strip()
    line = line.replace(" , ",",")
    line = line.replace('\t','')
    line = line.replace('\n','')
    data.append(line)

writeData = []
writeData.append(['Ticker', 'Date', 'Bid', 'Ask'])
for line in data:
    columns = line.split(",")
    if columns[4] == "YEN":
        columns[2] = float(line[2])/usdyen
        columns[3] = float(line[3])/usdyen
    writeData.append(columns)

csv = open("mktDataFormat.csv","w")

for line in writeData:
    csv.write(line[0] + "," + line[1] + "," + str(line[2]) + "," + str(line[3]) + "\n")
csv.close()








