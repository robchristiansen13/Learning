import numpy as np
import matplotlib.pyplot as plt

def createTheLine(inputParams):
    result = []
    m = -1
    b = 480
    for x in inputParams:
        y = m*x + b
        result.append(y)

def isYellowSigmoid(x,xtwo):
    m1 = 1
    m2 = 1
    b = -480
    t = m1*x+m2*xtwo + b
    sigmoid = 1/(1+np.math.exp(-t))
    return sigmoid

print("Our exp ~100%",isYellowSigmoid(255,255))
print("Our exp ~50%",isYellowSigmoid(240,240))
print("Our exp ~0%",isYellowSigmoid(220,220))

reds = list(range(127,255,2))
greens = list(range(127,255,2))

x = []
y = []
colors = []
sizes = []

for redShade in reds:
    for greenShade in greens:
        x.append(redShade)
        y.append(greenShade)
        sizes.append(400)#150
        probability = isYellowSigmoid(redShade,greenShade)
        probGreen = round(255*probability)
        probRed = round(255*probability)
        colors.append([probRed,probGreen,0])

colors = np.array(colors)

yline = createTheLine(x)
plt.plot(x,yline)
plt.scatter(x,y,c=colors/255.0, s = sizes)
plt.show()