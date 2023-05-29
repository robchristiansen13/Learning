import numpy as np
import matplotlib.pyplot as plt

randX = np.random.randint(120,260,200)
randXtwo = np.random.randint(120,260,200)

def isYellow(x,xtwo):
    m1 = -1
    m2 = -1
    b = 480
    result = m1*x+m2*xtwo + b
    return result<=0


plt.style.use(['seaborn-dark'])

colors = []
for i in range(0,200):
    rX = randX[i]
    rXtwo = randXtwo[i]
    if isYellow(rX,rXtwo):
        colors.append("yello")
    else:
        colors.append("blue")

plt.scatter(randX,randXtwo,c=colors)
plt.show()