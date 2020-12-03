import numpy as np
import matplotlib
matplotlib.use('tkagg')
import matplotlib.pyplot as plt
import random

X = [0]
t = [0]

tend = 1000

k = 2
gamma = 0.1

while t[-1] < tend:

        current_X = X[-1]

        rates = [k, gamma * current_X]
        rate_sum = sum(rates)

        tau = np.random.exponential(scale=1/rate_sum)

        t.append(t[-1] + tau)

        rand = random.uniform(0,1)

        # production event
        if rand * rate_sum > 0 and rand * rate_sum <= rates[0]:
                X.append(X[-1] + 1)

        # decay event
        elif rand * rate_sum > rates[0] and rand * rate_sum <= rates[0] + rates[1]:
                X.append(X[-1] - 1)



plt.plot(t,X)
plt.xlabel("time")
plt.ylabel("mRNA quantity")
plt.show()
