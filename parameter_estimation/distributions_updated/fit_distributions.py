import matplotlib.pyplot as plt
import scipy.stats
import csv
import numpy as np

# sudo pip3 install --upgrade scipy



# data = []

# with open("datasets/diner_quality.csv") as file:

#     reader = csv.reader(file, delimiter=',')
#     for row in reader:
#         data.append(float(row[0]))


# plt.hist(data, bins=100, density=True)
# plt.show()


# dist = scipy.stats.norm

# bounds = [(-100,100), (-100,100)]

# res = scipy.stats.fit(dist, data,bounds)
# print(res)

# res.plot()
# plt.show()





data = []

with open("datasets/customers_per_day.csv") as file:

    reader = csv.reader(file, delimiter=',')
    for row in reader:
        data.append(float(row[0]))


# plt.hist(data, bins=int(np.max(data)), density=True)
# plt.show()

# # easy way -- the one poisson parameter is the mean of the data
# print(np.mean(data))

dist = scipy.stats.poisson

bounds = [(-100,100)]

res = scipy.stats.fit(dist, data,bounds)
print(res)

res.plot()
plt.show()