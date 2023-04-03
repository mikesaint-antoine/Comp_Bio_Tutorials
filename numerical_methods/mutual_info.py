import random
import numpy as np




def entropy(X,bins):

    binned_dist = np.histogram(X,bins)[0]
    # print(binned_dist)

    probs = binned_dist / np.sum(binned_dist)
    # print(probs)

    probs = probs[np.nonzero(probs)]

    entropy = - np.sum(probs* np.log2(probs))

    return(entropy)




def joint_entropy(X,Y,bins):

    ## bin data, count number in each bin
    binned_dist = np.histogram2d(X,Y,bins)[0]

    # normalize counts to give probabilities
    probs = binned_dist / np.sum(binned_dist)

    # get rid of bins with 0
    probs = probs[np.nonzero(probs)]

    # calculate joint entropy
    joint_entropy = - np.sum(probs* np.log2(probs))


    return(joint_entropy)




def mutual_info(X,Y,bins):

    H_X = entropy(X,bins)
    H_Y = entropy(Y,bins)
    H_XY = joint_entropy(X,Y,bins)

    MI = H_X + H_Y - H_XY

    return(MI)



X = []
Y = []

# for i in range(1000):
#     x_draw = random.randint(0,1)
#     X.append(x_draw)

#     if x_draw == 0:
#         y_draw = random.randint(0,1)
#         Y.append(y_draw)
#     else:
#         y_draw = x_draw
#         Y.append(y_draw)       



X = []
Y = []

for i in range(100000):
    x_draw = np.random.normal(scale=100)
    # y_draw = np.random.normal(loc=x_draw)
    y_draw = np.random.normal()

    X.append(x_draw)
    Y.append(y_draw)


print(mutual_info(X,Y,10))