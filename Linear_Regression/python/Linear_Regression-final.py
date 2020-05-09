import numpy as np
import pandas as pd
from matplotlib import style
style.use("ggplot")

# initialize
df = pd.read_csv('linear_regression_data.txt', header=None, sep=',')
df.columns=['x1','x2','y']
x,y,z = df['x1'],df['x2'],df['y']
rowLen=len(df['x1'])
df.insert(loc=0, column='x0',value=np.ones(rowLen))
df=df.T


dxy = df.iloc[0:3,:]

dxy =dxy.values
ddt=np.dot(dxy, dxy.T)
iddt=np.linalg.inv(ddt)
t1=np.dot(iddt,dxy)

dy= df.iloc[3:4,:].values
w=np.dot(t1,dy.T)


result = pd.DataFrame(data= w, index=['w0','w1','w2'])
print("\nLinear Regression results are:" )
print(result)
