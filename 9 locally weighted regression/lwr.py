import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
import statsmodels.api as sm  #might need internet to download library learn with your own risk
import numpy as np
import math
x= np.linspace(0, 2 * math.pi, 100)
#print(x)
y= np.sin(x) + 0.3 * np.random.randn(100)
#print(y)
#print(len(y))
lowess=sm.nonparametric.lowess(y,x)
lowess_x=list(zip(*lowess))[0]
lowess_y=list(zip(*lowess))[1]
f=interp1d(lowess_x,lowess_y,bounds_error=False)
xnew=[i/10.0 for i in range(100)]
ynew=f(xnew)
plt.plot(x,y,'o')
plt.plot(lowess_x,lowess_y,'+')
plt.plot(xnew,ynew,"-")
plt.show()

