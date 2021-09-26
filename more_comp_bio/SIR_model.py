import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint



t = np.linspace(0,500, num=1000)

beta = 0.04
gamma = 0.01


params = [beta,gamma]


y0 = [100, 1, 0]



def sim(variables, t, params):

    S = variables[0]
    I = variables[1]
    R = variables[2]

    N = S + I + R

    beta = params[0]
    gamma = params[1]

    dSdt = -beta * I * S / N
    dIdt = beta * I * S / N - gamma * I
    dRdt = gamma * I

    return([dSdt, dIdt, dRdt])


y = odeint(sim, y0, t, args=(params,))



f,(ax1,ax2,ax3) = plt.subplots(3)

line1, = ax1.plot(t,y[:,0]) # S
line2, = ax2.plot(t,y[:,1]) # I
line3, = ax3.plot(t,y[:,2]) # R



ax1.set_ylabel("S")
ax2.set_ylabel("I")
ax3.set_ylabel("R")
ax3.set_xlabel("Time")

plt.show()
