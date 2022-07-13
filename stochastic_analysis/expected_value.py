import random
import numpy as np


payouts = []

for trial in range(10000):

    if random.random()>0.5:
        payout = 5
    else:
        payout = -50

    payouts.append(payout)


print("Expected payout:")
print(np.mean(payouts))
