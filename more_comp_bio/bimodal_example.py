import matplotlib
matplotlib.use('tkagg')
import matplotlib.pyplot as plt
import numpy as np
import random



def grow_colony(X, params, tend):

        r = params[0]
        K = params[1]
        gamma = params[2]

        t = [0]

        while t[-1] < tend and X[-1]>0:

                current_X = X[-1]

                rates = [r*current_X, r*current_X**2/K + gamma*current_X]

                rate_sum = sum(rates)

                tau = np.random.exponential(scale=1/rate_sum)

                t.append(t[-1] + tau)

                rand = random.uniform(0,1)

                if rand * rate_sum <= rates[0]:
                        X.append(X[-1] + 1)

                else:
                        X.append(X[-1] - 1)

        return([t, X])



cell_counts = []

for i in range(10000):

        X_in = [1]
        r = 1
        K = 100
        gamma = 0.05

        params = [r, K, gamma]

        tend = 12


        [t_out, X_out] = grow_colony(X_in, params, tend)

        cell_counts.append(X_out[-1])



plt.hist(cell_counts, bins=np.max(cell_counts)+1)
plt.show()
