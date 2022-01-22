import matplotlib.pyplot as plt
import scipy.stats
import csv
import numpy as np

# data = []
#
# with open("diner_quality.csv") as file:
#
#     reader = csv.reader(file, delimiter=',')
#     for row in reader:
#         data.append(float(row[0]))
#
#
# plt.hist(data, bins=100, density=True)
#
#
# [mean_fit, std_fit] = scipy.stats.norm.fit(data)
#
# print(mean_fit)
# print(std_fit)
#
# x = np.linspace(np.min(data), np.max(data))
#
# plt.plot(x, scipy.stats.norm.pdf(x, mean_fit, std_fit),)
#
# plt.xlabel("Restaurant Quality")
# plt.ylabel("Probability Density")
#
# plt.show()


###################################################





data = []

with open("pizza_shop_quality.csv") as file:

    reader = csv.reader(file, delimiter=',')
    for row in reader:
        data.append(float(row[0]))


plt.hist(data, bins=100, density=True)




[a_fit, loc_fit, scale_fit] = scipy.stats.gamma.fit(data)

print(a_fit)
print(loc_fit)
print(scale_fit)

x = np.linspace(np.min(data), np.max(data))

plt.plot(x, scipy.stats.gamma.pdf(x, a_fit, loc=loc_fit, scale=scale_fit),)

plt.xlabel("Restaurant Quality")
plt.ylabel("Probability Density")

plt.show()
