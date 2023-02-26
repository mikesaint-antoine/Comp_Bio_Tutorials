import matplotlib.pyplot as plt
from scipy.integrate import odeint
import numpy as np

m_init = 0
p_init = 0
tend = 200


k_m = 0.4
gamma_m = 0.1
k_p = 0.2
gamma_p = 0.05

M = [m_init]
P = [p_init]
t = [0]

delta_t = 0.5


while t[-1] < tend:

    next_M = M[-1] + (k_m - gamma_m * M[-1]) * delta_t
    M.append(next_M)

    next_P = P[-1] + (k_p * M[-1] - gamma_p * P[-1]) * delta_t
    P.append(next_P)  

    next_t = t[-1] + delta_t
    t.append(next_t)



f,ax = plt.subplots(1)

line1, = ax.plot(t,M, color="b", label="Euler M")
line2, = ax.plot(t,P, color="r", label="Euler P")

ax.set_ylabel("Abundance")
ax.set_xlabel("Time")
# ax.legend(handles=[line1,line2])
# plt.show()





y0 = [m_init,p_init]
t = np.linspace(0,tend,num=100)
params = [k_m, gamma_m,k_p,gamma_p]

def sim(variables, t, params):

    M = variables[0]
    P = variables[1]

    k_m = params[0]
    gamma_m = params[1]
    k_p = params[2]
    gamma_p = params[3]

    dMdt = k_m - gamma_m * M
    dPdt = k_p * M - gamma_p * P




    return([dMdt,dPdt])


y = odeint(sim, y0, t, args=(params,))

line3, = ax.plot(t,y[:,0], color="black", label="scipy M",linestyle="dashed")
line4, = ax.plot(t,y[:,1], color="black", label="scipy P",linestyle="dashed")

ax.legend(handles=[line1,line2,line3,line4])
plt.show()


