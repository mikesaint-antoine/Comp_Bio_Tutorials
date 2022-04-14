import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import sys

y0 = [10,1] # [fish, bears] units in hundreds

t = np.linspace(0,50,num=1001)

alpha = 1.1

beta = 0.4
delta = 0.1
gamma = 0.4


params = [alpha, beta, delta, gamma]

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


y = odeint(sim, y0, t, args=(params,))


data_t = []
data_fish = []
data_bears = []

for i in range(t.shape[0]):
    print(t[i])
    print(y[i,0])
    print(y[i,1])
    print()
    print()

    if i%20==0:
        data_t.append(t[i])
        data_fish.append(np.random.normal(loc=y[i,0], scale=0.2,))
        data_bears.append(np.random.normal(loc=y[i,1], scale=0.2,))






print(y.shape)
print(t.shape)

for row in data_t:
    print(row)


# sys.exit()

f,(ax1,ax2) = plt.subplots(2)

line1 = ax1.scatter(data_t,data_fish, c="b")



line2 = ax2.scatter(data_t,data_bears, c="r")

ax1.set_ylabel("Fish (hundreds)")
ax2.set_ylabel("Bears (hundreds)")
ax2.set_xlabel("Time (years)")
plt.savefig("population_data.pdf")

plt.show()


# f,(ax1,ax2) = plt.subplots(2)
#
# line1, = ax1.plot(t,y[:,0], color="b")
#
#
#
# line2, = ax2.plot(t,y[:,1], color="r")
#
# ax1.set_ylabel("Fish (hundreds)")
# ax2.set_ylabel("Bears (hundreds)")
# ax2.set_xlabel("Time (years)")
#
# plt.show()



# making CSV
f = open('population_data.csv', "w")

f.write("year,fish_hundreds,bears_hundreds\n")

for i in range(len(data_t)):
    f.write("%s,%s,%s\n" % (data_t[i],data_fish[i],data_bears[i]))

f.close()
