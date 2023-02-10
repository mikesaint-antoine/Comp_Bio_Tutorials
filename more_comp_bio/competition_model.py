import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint


# y0 = [10,10] # [species 1 (x1), species 2 (x2)] units in hundreds

t = np.linspace(0,50,num=1000) # unitless time (maybe weeks or months?)


# params
r1 = 2
r2 = 1
a1 = 2
a2 = 5
k1 = 100
k2 = 150


x1_s = (k1-a1*k2) / (1-a2*a1)
x2_s = (k2-a2*k1) / (1-a1*a2)


y0 = [x1_s,x2_s] # [species 1 (x1), species 2 (x2)] units in hundreds


params = [r1,r2,a1,a2,k1,k2]



def sim(variables,t,params):

    # species1 population level
    x1 = variables[0]

    # species2 population level
    x2 = variables[1]

    r1 = params[0]
    r2 = params[1]
    a1 = params[2]
    a2 = params[3]
    k1 = params[4]
    k2 = params[5]

    dx1dt = r1 * x1 * (1 - (x1 + a1*x2)/k1)
    dx2dt = r2 * x2 * (1 - (x2 + a2*x1)/k2)

    return([dx1dt,dx2dt])


y = odeint(sim, y0, t,args=(params,))

# print(y)


f,(ax1,ax2) = plt.subplots(2)
line1, = ax1.plot(t,y[:,0], color="b")
line2, = ax2.plot(t,y[:,1], color="r")
ax1.set_ylabel("x1")
ax2.set_ylabel("x2")
ax2.set_xlabel("Time")

plt.show()