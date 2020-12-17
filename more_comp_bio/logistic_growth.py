import numpy as np
import matplotlib
matplotlib.use('tkagg')
import matplotlib.pyplot as plt
from scipy.integrate import odeint


y0 = [1] # start with 1 cell

t = np.linspace(0,500,num=1000)

r = 0.05
K = 100000


params = [r,K]

def sim(variables,t,params):

    X = variables[0]

    r = params[0]
    K = params[1]

    dXdt = r*X * (1 - X/K)

    return([dXdt])


y = odeint(sim,y0, t, args=(params,))


plt.plot(t,y[:,0])
plt.xlabel("Time")
plt.ylabel("Cells")
plt.show()
