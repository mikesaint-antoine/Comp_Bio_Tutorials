import numpy as np
import matplotlib
matplotlib.use('tkagg')
import matplotlib.pyplot as plt
import random



game_counts = []


for simulation_count in range(10000):

    my_money = 100


    game_count = 0

    while my_money > 0:

        if random.randint(1,38) <= 18:
            my_money = my_money + 5

        else:
            my_money = my_money - 5

        game_count = game_count + 1


    # print("Simulation Over")
    # print("Money Left:")
    # print(my_money)
    # print("Number of Games:")
    # print(game_count)

    game_counts.append(game_count)

print("mean:")
print(np.mean(game_counts))
print("standard deviation:")
print(np.std(game_counts))


plt.hist(game_counts, bins=int(np.max(game_counts)/4))

plt.show()
