import matplotlib.pyplot as plt
import numpy as np
import csv
import scipy.optimize
from scipy.integrate import odeint


## read data

timepoints = []
cell_counts = []


with open("cell_count_data.csv") as file:
    reader = csv.reader(file, delimiter=",")

    next(reader)

    for row in reader:
        timepoints.append(float(row[0]))
        cell_counts.append(float(row[1]))





f,(ax1) = plt.subplots(1)

line1 = ax1.scatter(timepoints,cell_counts, c="b", s=6)

ax1.set_ylabel("Cell Counts")
ax1.set_xlabel("Time (hours)")
#
# plt.show()


def sim(variables,t,params):

    X = variables[0]

    r = params[0]
    K = params[1]

    dXdt = r*X * (1 - X/K)

    return([dXdt])




def loss_function(params, timepoints, cell_counts):

    y0 = [cell_counts[0]]

    t = np.linspace(timepoints[0], timepoints[-1], num=len(timepoints))

    output = odeint(sim, y0, t, args=(params,))

    loss = 0

    for i in range(len(timepoints)):
        data_count = cell_counts[i]
        model_count = output[i,0]

        res = (data_count - model_count)**2

        loss += res

    return(loss)


params0 = np.array([1,100])
minimum = scipy.optimize.fmin(loss_function, params0, args=(timepoints,cell_counts))
print(minimum)





r_fit = minimum[0]
K_fit = minimum[1]


params = [r_fit, K_fit]

y0 = [cell_counts[0]]


t = np.linspace(timepoints[0], timepoints[-1], num=1000)

output = odeint(sim, y0, t, args=(params,))

line1, = ax1.plot(t,output[:,0], color="r")

ax1.set_ylabel("Cell Counts")
ax1.set_xlabel("Time (hours)")

plt.show()
