import matplotlib.pyplot as plt
import numpy as np
import math
import pandas as pd
from matplotlib import style

style.use("ggplot")

# initialize
df = pd.read_csv('logistical_regression_data.txt', header=None, sep=',')
df.columns=['x1','x2','x3','rd','r']
del df['rd']
rowLen=len(df['x1'])
df.insert(loc=0, column='x0',value=pd.Series(np.ones((rowLen))))
w=np.random.random([4,1])

# set a = 0.001
a = 0.005


iterations = 100

i=0
dEin=np.zeros((4,1))
num = 0
lr = []

while i < iterations:
    i+=1
    num = 0
    dEin = np.zeros((4,1))
    for index, point in df.iterrows():
        s = np.dot(point.iloc[0:4], w)
        poss=np.exp(s) / (np.exp(s)+1)
        if (poss-0.5)*point['r'] < 0 :
            num+=1
        temp1=np.reciprocal(1+math.exp(point['r']*(np.dot(point.iloc[0:4],w))))*point['r']*point.iloc[0:4]
        dEin = np.add(dEin,temp1.values.reshape(4,1))
    dEin = dEin * (-1/rowLen)
    w= w - a*dEin
    lr.append(num)

print("Logistical Regression Algorithm:")
dw = pd.DataFrame(data=w,index=['w0','w1','w2','w3'])
print(dw)




axisX = range(len(lr))
fig = plt.figure()
ax1 = fig.add_subplot(111)

ax1.set_title('Logistical Learning Algorithm')

plt.xlabel('Iterations')

plt.ylabel('Violet Points')

ax1.scatter(axisX,lr,c = 'r',marker = '.')

plt.legend('x')

plt.show()