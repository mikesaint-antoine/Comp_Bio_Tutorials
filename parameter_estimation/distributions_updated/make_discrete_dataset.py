import matplotlib.pyplot as plt
import scipy.stats
import csv
import sys
import numpy as np



mu = 5

data = scipy.stats.poisson.rvs(mu,size=1000)



plt.hist(data,bins=np.max(data))
plt.ylabel("Occurrences")
plt.xlabel("Number of Customers (per day)")
plt.savefig("customers_per_day.pdf")



f = open('customers_per_day.csv', "w")
for i in range(data.shape[0]):
    f.write("%s\n" % (data[i]))
f.close()
