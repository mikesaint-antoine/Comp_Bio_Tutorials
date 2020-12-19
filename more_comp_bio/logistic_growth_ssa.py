import numpy as np
import matplotlib
matplotlib.use('tkagg')
import matplotlib.pyplot as plt
import random
from scipy.integrate import odeint



X = [1]
t = [0]


tend = 400

r = 0.05
K = 100

while t[-1] < tend:

        current_X = X[-1]

        rates = [r*current_X, r*current_X**2 / K]

        rate_sum = sum(rates)

        tau = np.random.exponential(scale=1/rate_sum)

        t.append(t[-1] + tau)

        rand = random.uniform(0,1)

        if rand * rate_sum <= rates[0]:
                X.append(X[-1] + 1)

        else:
                X.append(X[-1] - 1)


plt.plot(t,X)
plt.xlabel("Time")
plt.ylabel("Cells")





y0 = [1] # start with 1 cell

t = np.linspace(0,tend,num=1000)

# r = 0.05
# K = 100000


params = [r,K]

def sim(variables,t,params):

    X = variables[0]

    r = params[0]
    K = params[1]

    dXdt = r*X * (1 - X/K)

    return([dXdt])


y = odeint(sim,y0, t, args=(params,))




plt.plot(t,y[:,0])













plt.show()
