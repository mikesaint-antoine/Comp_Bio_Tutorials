import numpy as np
import matplotlib
matplotlib.use('tkagg')
import matplotlib.pyplot as plt
from scipy.integrate import odeint


y0 = [0,0] # 0 mRNA, 0 protein

t = np.linspace(0,200,num=100)

k_m = 0.2
gamma_m = 0.05
k_p = 0.4
gamma_p = 0.1

params = [k_m, gamma_m, k_p, gamma_p]

def sim(variables, t, params):

    m = variables[0]
    p = variables[1]

    k_m = params[0]
    gamma_m = params[1]
    k_p = params[2]
    gamma_p = params[3]

    dmdt = k_m - gamma_m * m
    dpdt = k_p * m - gamma_p * p

    return([dmdt,dpdt])



y = odeint(sim, y0, t, args=(params,))


f,ax = plt.subplots(1)

line1, = ax.plot(t,y[:,0], color="b", label="M")



line2, = ax.plot(t,y[:,1], color="r", label="P")

ax.set_ylabel("Abundance")
ax.set_xlabel("Time")

ax.legend(handles=[line1,line2])

plt.show()
