import matplotlib
matplotlib.use('tkagg')
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import numpy as np


y0 = [0,0]

t = np.linspace(0,200, num=100)

k_1 = 0.5
gamma_1 = 0.1
k_2 = 0.5
gamma_2 = 0.05
n = 5
c = 5

params = [k_1, gamma_1, k_2, gamma_2, n ,c]


def sim(variables, t, params):

    G1 = variables[0]
    G2 = variables[1]

    k_1 = params[0]
    gamma_1 = params[1]
    k_2 = params[2]
    gamma_2 = params[3]
    n = params[4]
    c = params[5]


    dG1dt = k_1 - gamma_1 * G1

    dG2dt = (G1**n / (c**n + G1**n)) * k_2 - gamma_2 * G2

    return([dG1dt, dG2dt])


y = odeint(sim, y0, t, args=(params,))


f, ax = plt.subplots(1)

line1, = ax.plot(t , y[:,0], color="b",label="G1")
line2, = ax.plot(t , y[:,1], color="r",label="G2")

ax.set_ylabel('Number')
ax.set_xlabel('Time')

ax.legend(handles=[line1,line2])

plt.show()
