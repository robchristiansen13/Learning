import pandas as pd
import matplotlib.pyplot as pd
from matplotlib import pyplot as plt

data = pd.read_excel("LungCancerStatistics.xlsx")
print(data)

x = data["Cigarettes a day"].values
xTwo = data["Years Smoking"].values

result = data["Lung Cancer"].values

colors = []
for value in result:
    if value == "Yes":
        colors.append("red")
    if value == "No":
        colors.append("Green")

plt.scatter(x,xTwo,c=colors)
plt.show