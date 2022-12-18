import numpy as np
import matplotlib.pyplot as plt
import random

## toggle switch ssa

G1 = [0]
G2 = [0]
t = [0]


tend = 1000

k_1 = 1
gamma_1 = 0.2
k_2 = 1
gamma_2 = 0.2


c = 1
h = 9


while t[-1] < tend:

    props = [(c**h / (c**h + G2[-1]**h)) * k_1, gamma_1 * G1[-1], \
    (c**h / (c**h + G1[-1]**h)) * k_2, gamma_2 * G2[-1]]


    prop_sum = sum(props)


    tau = np.random.exponential(scale=1/prop_sum)

    t.append(t[-1] + tau)


    rand = random.uniform(0,1)


    # G1 production event
    if rand * prop_sum <= props[0]:
            G1.append(G1[-1] + 1)
            G2.append(G2[-1])

    # G1 decay event
    elif rand * prop_sum > props[0] and rand * prop_sum <= sum(props[:2]):
            G1.append(G1[-1] - 1)
            G2.append(G2[-1])

    # G2 production event
    elif rand * prop_sum > sum(props[:2]) and rand * prop_sum <= sum(props[:3]):
            G1.append(G1[-1])
            G2.append(G2[-1] + 1)

    # G2 decay event
    elif rand * prop_sum > sum(props[:3]) and rand * prop_sum <= sum(props[:4]):
            G1.append(G1[-1])
            G2.append(G2[-1] - 1)    




f, (ax1, ax2) = plt.subplots(2, sharex=True, sharey=False)
line1, = ax1.plot(t , G1, color="b",label="G1")
line2, = ax2.plot(t , G2, color="r",label="G2")
ax1.set_ylabel('G1')
ax2.set_ylabel('G2')

ax2.set_xlabel('Time')
plt.show()
