import matplotlib
matplotlib.use('tkagg')
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import numpy as np

y0 = [0,0,0]

t = np.linspace(0,200, num=100)

k_1 = 0.5
gamma_1 = 0.1
k_2 = 0.5
gamma_2 = 0.1
k_3 = 0.5
gamma_3 = 0.1
n = 9
c = 1




params = [k_1, gamma_1, k_2, gamma_2, k_3, gamma_3, n, c]

def sim(variables, t, params):
    G1 = variables[0]
    G2 = variables[1]
    G3 = variables[2]

    k_1 = params[0]
    gamma_1 = params[1]
    k_2 = params[2]
    gamma_2 = params[3]
    k_3 = params[4]
    gamma_3 = params[5]
    n = params[6]
    c = params[7]


    dG1dt = (c**n / (c**n + G3**n)) * k_1 - gamma_1 * G1
    dG2dt = (G1**n / (c**n + G1**n)) * k_2 - gamma_2 * G2
    dG3dt = (G2**n / (c**n + G2**n)) * k_3 - gamma_3 * G3

    return([dG1dt,dG2dt,dG3dt])





y = odeint(sim,y0,t, args=(params,))



f, (ax1, ax2, ax3) = plt.subplots(3, sharex=True, sharey=False)

line1, = ax1.plot(t , y[:,0], color="b",label="G1")
line2, = ax2.plot(t , y[:,1], color="r",label="G2")
line3, = ax3.plot(t , y[:,2], color="g",label="G3")

ax1.set_ylabel('Number')
ax1.set_xlabel('Time')

ax1.legend(handles=[line1,line2,line3])

plt.show()
