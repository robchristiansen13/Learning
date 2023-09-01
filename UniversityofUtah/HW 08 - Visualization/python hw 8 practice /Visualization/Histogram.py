import matplotlib.pyplot as plt
import pandas as pd


spx = pd.read_csv("spx_daily.csv",index_col="Date",parse_dates=True)
spx = spx[["Close"]]
spx["pctChange"] = spx["Close"].pct_change()
spx = spx.drop("Close",axis=1)

values = spx["pctChange"].values
values = values[1:]
print(spx)

plt.hist(values,50,facecolor="red",alpha=0.7)

mean = spx["pctChange"].mean()
varience = spx['pctChange'].std()

plt.axvline(x=mean)
plt.axvline(x=mean+3*varience)
plt.axvline(x=mean+4*varience)
plt.axvline(x=mean-3*varience)
plt.axvline(x=mean-4*varience)

plt.show()