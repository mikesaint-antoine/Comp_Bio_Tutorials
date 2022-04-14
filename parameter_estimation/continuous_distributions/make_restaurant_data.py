import matplotlib.pyplot as plt
import scipy.stats
import csv
import sys


# mean  = 10
# std = 3
# data = scipy.stats.norm.rvs(mean,std,size=10000)
#
#
# plt.hist(data,bins=100)
# plt.ylabel("Occurrences")
# plt.xlabel("Diner Quality")
# plt.savefig("diner_quality.pdf")
# # plt.show()
#
#
#
# f = open('diner_quality.csv', "w")
# for i in range(data.shape[0]):
#     f.write("%s\n" % (data[i]))
# f.close()
#
#
#
# sys.exit()


data = scipy.stats.gamma.rvs(2, loc=3, scale=3,size=10000)


plt.hist(data,bins=100)
plt.ylabel("Occurrences")
plt.xlabel("Pizza Shop Quality")
plt.savefig("pizza_shop_quality.pdf")



f = open('pizza_shop_quality.csv', "w")
for i in range(data.shape[0]):
    f.write("%s\n" % (data[i]))
f.close()
