import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import sys



y0 = [1] # start with 1 cell

t = np.linspace(0,100,num=101)

r = 0.2
K = 2000


params = [r,K]

def sim(variables,t,params):

    X = variables[0]

    r = params[0]
    K = params[1]

    dXdt = r*X * (1 - X/K)

    return([dXdt])


y = odeint(sim,y0, t, args=(params,))




data_t = []
data_X = []

for i in range(t.shape[0]):
    print(t[i])
    print(y[i,0])
    print()
    print()

    data_t.append(t[i])
    data_X.append(int(abs(np.random.normal(loc=y[i,0], scale=50,))))






print(y.shape)
print(t.shape)

for row in data_t:
    print(row)


# sys.exit()

f,(ax1) = plt.subplots(1)

line1 = ax1.scatter(data_t,data_X, c="b",s=6)




ax1.set_ylabel("Cell Count")
ax1.set_xlabel("Time (hours)")
plt.savefig("cell_count_data.pdf")

# plt.show()






# making CSV
f = open('cell_count_data.csv', "w")

f.write("time,cell_count\n")

for i in range(len(data_t)):
    f.write("%s,%s\n" % (data_t[i],data_X[i]))

f.close()
