import matplotlib.pyplot as plt
import numpy as np
import csv
import scipy.optimize
from scipy.integrate import odeint


## read data

years = []
fish_pop = []
bears_pop = []

with open("population_data.csv") as file:

    reader = csv.reader(file, delimiter=',')

    # skip header
    next(reader)

    for row in reader:
        years.append(float(row[0]))
        fish_pop.append(float(row[1]))
        bears_pop.append(float(row[2]))





f,(ax1,ax2) = plt.subplots(2)

line1 = ax1.scatter(years,fish_pop, c="b")
line2 = ax2.scatter(years,bears_pop, c="r")

ax1.set_ylabel("Fish (hundreds)")
ax2.set_ylabel("Bears (hundreds)")
ax2.set_xlabel("Time")
#
# plt.show()


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



def loss_function(params, years,fish_pop, bears_pop):

    y0 = [fish_pop[0], bears_pop[0]]

    t = np.linspace(years[0], years[-1], num=len(years))

    output = odeint(sim, y0, t, args=(params,))

    loss = 0

    for i in range(len(years)):
        data_fish = fish_pop[i]
        model_fish = output[i,0]

        data_bears = bears_pop[i]
        model_bears = output[i,1]

        res = (data_fish - model_fish)**2 + (data_bears - model_bears)**2

        loss += res

    return(loss)



params0 = np.array([1,1,1,1])
minimum = scipy.optimize.fmin(loss_function, params0, args=(years,fish_pop, bears_pop))

print(minimum)

alpha_fit = minimum[0]
beta_fit = minimum[1]
delta_fit = minimum[2]
gamma_fit = minimum[3]

params = [alpha_fit, beta_fit, delta_fit, gamma_fit]

y0 = [fish_pop[0], bears_pop[0]]


t = np.linspace(years[0], years[-1], num=1000)

output = odeint(sim, y0, t, args=(params,))



line1, = ax1.plot(t,output[:,0], color="b")
line2, = ax2.plot(t,output[:,1], color="r")

ax1.set_ylabel("Fish (hundreds)")
ax2.set_ylabel("Bears (hundreds)")
ax2.set_xlabel("Time")

plt.show()
