import numpy as np
import matplotlib.pyplot as plt

def createTheLine(inputParams):
    result = []
    m = -1
    b = 480
    for x in inputParams:
        y = m*x + b
        result.append(y)

    return result

reds = list(range(127,255,2))
greens = list(range(127,255,2))

x = []
y = []
colors = []
sizes = []

plt.style.use(['seaborn-dark'])

for redShade in reds:
    for greenShade in greens:
        x.append(redShade)
        y.append(greenShade)
        sizes.append(400)#150
        colors.append([redShade,greenShade,0])

colors = np.array(colors)

yline = createTheLine(x)
plt.plot(x,yline)
plt.scatter(x,y,c=colors/255.0, s = sizes)
plt.show()
