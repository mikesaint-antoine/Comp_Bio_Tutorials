import matplotlib.pyplot as plt
import scipy.stats
import csv
import numpy as np


data = []

with open("customers_per_day.csv") as file:

    reader = csv.reader(file, delimiter=',')
    for row in reader:
        data.append(float(row[0]))


plt.hist(data, bins=int(np.max(data)), density=True, alpha=0.5)

# plt.show()



def loss_function(params, data_in):

    mu = params[0]

    loss = 0

    for i in range(len(data_in)):

        loglikelihood = scipy.stats.poisson.logpmf(data_in[i], mu)

        loss_to_add = -loglikelihood

        loss += loss_to_add

    return(loss)



params0 = np.array([20])
minimum = scipy.optimize.fmin(loss_function, params0, args=(data,))

mu_fit = minimum[0]

print("mu_fit")
print(mu_fit)



x = list(range(int(np.min(data)), int(np.max(data))+1))
plt.scatter(x, scipy.stats.poisson.pmf(x, mu_fit),color="red")
plt.xlabel("Number of Customers (per day)")
plt.ylabel("Probability")
plt.show()
