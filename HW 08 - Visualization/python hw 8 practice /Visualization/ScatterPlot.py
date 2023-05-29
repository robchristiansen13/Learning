import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("sf_pe_salaries_2011.csv",index_col="Id")
data["BasePay"] = data["BasePay"].replace("Not Provided","0")
data = data.dropna()
# data = data.fillna()

data["BasePay"] = data["BasePay"].astype(float)
print(data.head())

y = data["BasePay"].values
ySorted = sorted(y)
x = data.index/data.index.max()*100

plt.scatter(x,ySorted)
plt.grid()
plt.show()