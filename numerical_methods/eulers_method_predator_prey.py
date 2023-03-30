import matplotlib.pyplot as plt
from scipy.integrate import odeint
import numpy as np


X_init = 10
Y_init = 1
tend = 50

a = 1.1
b = 0.4
c = 0.1
h = 0.4

X = [X_init]
Y = [Y_init]
t = [0]


# delta_t = 0.5
# delta_t = 0.1
delta_t = 0.01


while t[-1] < tend:

    next_X = X[-1] + (a * X[-1] - b * X[-1] * Y[-1]) * delta_t # next X is current X plus delta X
    X.append(next_X)

    next_Y = Y[-1] + (c * X[-1] * Y[-1] - h * Y[-1]) * delta_t # next Y is current Y plus delta Y
    Y.append(next_Y)

    next_t = t[-1] + delta_t
    t.append(next_t)




f,ax = plt.subplots(1)

line1, = ax.plot(t,X, color="b", label="Euler X")
line2, = ax.plot(t,Y, color="r", label="Euler Y")

ax.set_ylabel("Abundance")
ax.set_xlabel("Time")
# ax.legend(handles=[line1,line2])
# plt.show()





####################
y0 = [X_init,Y_init]
t = np.linspace(0,tend,num=100)
params = [a, b,c,h]

def sim(variables, t, params):

    x = variables[0]

    y = variables[1]


    alpha = params[0]
    beta = params[1]
    delta = params[2]
    gamma = params[3]

    dxdt = alpha * x - beta * x * y
    dydt = delta * x * y - gamma * y

    return([dxdt, dydt])



y = odeint(sim, y0, t, args=(params,))

line3, = ax.plot(t,y[:,0], color="black", label="scipy X",linestyle="dashed")
line4, = ax.plot(t,y[:,1], color="black", label="scipy Y",linestyle="dashed")

ax.legend(handles=[line1,line2,line3,line4])
plt.show()