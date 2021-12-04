import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint


y0 = [10,1] # [fish, bears] units in hundreds

t = np.linspace(0,50,num=1000)

alpha = 1.1
beta = 0.4
delta = 0.1
gamma = 0.4


params = [alpha, beta, delta, gamma]

def sim(variables, t, params):

    # fish population level
    x = variables[0]

    # bear population level
    y = variables[1]


    alpha = params[0]
    beta = params[1]
    delta = params[2]
    gamma = params[3]

    dxdt = alpha * x - beta * x * y
    dydt = delta * x * y - gamma * y

    return([dxdt, dydt])


# alpha = 1.1
y = odeint(sim, y0, t, args=(params,))



params = [0.9, beta, delta, gamma]
y2 = odeint(sim, y0, t, args=(params,))


params = [1.3, beta, delta, gamma]
y3 = odeint(sim, y0, t, args=(params,))






f,(ax1) = plt.subplots(1)



line1, = ax1.plot(y[:,0],y[:,1], color="b", label="alpha = 1.1")

line2, = ax1.plot(y2[:,0],y2[:,1], color="r", label="alpha = 0.9")

line3, = ax1.plot(y3[:,0],y3[:,1], color="g", label="alpha = 1.3")

leg = plt.legend()

ax1.set_xlabel("Prey (hundreds)")
ax1.set_ylabel("Predators (hundreds)")


plt.show()
