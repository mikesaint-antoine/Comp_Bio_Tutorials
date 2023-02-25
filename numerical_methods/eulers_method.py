import matplotlib.pyplot as plt
from scipy.integrate import odeint
import numpy as np



m_init = 0
tend = 200

k = 0.2
gamma = 0.05


M = [m_init]
t = [0]

delta_t = 0.5


while t[-1] < tend:

    next_M = M[-1] + (k - gamma*M[-1]) * delta_t

    M.append(next_M)

    next_t = t[-1] + delta_t

    t.append(next_t)



f,ax = plt.subplots(1)

line1, = ax.plot(t,M, color="b", label="Euler")
ax.set_ylabel("Abundance")
ax.set_xlabel("Time")
# ax.legend(handles=[line1])
# plt.show()
    




y0 = [m_init]
t = np.linspace(0,tend,num=100)
params = [k, gamma]

def sim(variables, t, params):

    m = variables[0]
    k = params[0]
    gamma = params[1]
    dmdt = k - gamma * m
    return([dmdt])


y = odeint(sim, y0, t, args=(params,))

line2, = ax.plot(t,y[:,0], color="r", label="scipy odeint",linestyle="dashed")

ax.legend(handles=[line1,line2])
plt.show()
