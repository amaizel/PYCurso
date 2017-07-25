def f(y,t):
    x,v = y
    dvdt = [v,-4*x]
    return dvdt

from scipy import *
from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt
x0,v0 = 0.0,1.0
ts = np.linspace(0,50,1000)

y = odeint(f,[x0,v0],ts)
#y.set_initial_value(x0,t0)
#y.integrate(y)
print(y)
plt.plot(ts,y)
#plt.plot(y[1],ts)
plt.show()

x = 0.0
v = 1.0
dt = 50.0/1000
solution = []
error = []
for t in ts:
   # x += v*dt
    v += -4*x*dt
    x += v*dt
    err = (cos(t) - x)
    print(x)
    solution.append([x,v])
    error.append(err)
plt.plot(ts,error)
plt.plot(ts,solution)
plt.show()
    
    
