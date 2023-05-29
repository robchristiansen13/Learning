import pandas as pd
import matplotlib.pyplot as plt

oil = pd.read_csv("oilPrices.csv",index_col="Date",parse_dates=True)
rub = pd.read_csv("usdPrices.csv",index_col="Date",parse_dates=True)

join = oil.join(rub,rsuffix="UsdRub",how="inner")
join.plot()
# print(join.head(10))

# oilY = join["Price"].values
# rubY = join["PriceUsdRub"].values
# index = rub.index
# print(oilY)
# print(index)
#
# plt.plot(index, oilY, "r--", label="Price of Oil in USD")
# plt.plot(index,rubY,"g",label="Price of USD in RUB")
# plt.legend()
plt.show()
