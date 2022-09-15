import numpy as np
import random
import matplotlib.pyplot as plt
import math



## calculate euclidean distance between points

# [1,3]
# [2,4]

# [3,4,5,6]
# [5,6,7,8]

# sqrt((1-2)**2 + (3-4)**2 )

def calc_distance(first,second):

    sum = 0

    for i in range(len(first)):
        sum += (first[i] - second[i])**2

    dist = math.sqrt(sum)
    return(dist)







## make some example data

sample_size = 100

data = []

for i in range(sample_size):
    num1 = np.round(random.uniform(1,5), decimals=3)
    num2 = np.round(random.uniform(1,5), decimals=3)

    data.append([num1,num2])


## edit some random data points to make them outliers

randint = random.randrange(0,sample_size)
data[randint][0] = data[randint][0]+10
data[randint][1] = data[randint][1]+10


randint = random.randrange(0,sample_size)
data[randint][0] = data[randint][0]-12
data[randint][1] = data[randint][1]-5


randint = random.randrange(0,sample_size)
data[randint][0] = data[randint][0]-6
data[randint][1] = data[randint][1]+7


randint = random.randrange(0,sample_size)
data[randint][0] = data[randint][0]+6
data[randint][1] = data[randint][1]-7


# copy_to_plot = np.array(data)
# plt.scatter(copy_to_plot[:,0], copy_to_plot[:,1])
# plt.show()


N = len(data)

dist_mat = np.zeros(shape=(N,N))



for i in range(N):
    for j in range(i+1,N):
        dist = calc_distance(data[i],data[j])

        dist_mat[i,j] = dist
        dist_mat[j,i] = dist


k = 3
avg_dist_list = []

outlier_inds = []

for i in range(N):
    all_dists = list(dist_mat[i,:])

    all_dists = sorted(all_dists)

    neighbor_dists = all_dists[1:k+1]

    avg_dist = np.mean(neighbor_dists)

    avg_dist_list.append(avg_dist)

    if avg_dist>3:
        outlier_inds.append(i)


print(outlier_inds)

## plot to see visually how far away outliers are

# plt.hist(avg_dist_list,bins=10)
# plt.show()




## removing outliers

# outlier_inds = sorted(outlier_inds,reverse=True)

# for ind in outlier_inds:
#     del[data[ind]]



copy_to_plot = np.array(data)
plt.scatter(copy_to_plot[:,0], copy_to_plot[:,1])
plt.scatter(copy_to_plot[outlier_inds,0], copy_to_plot[outlier_inds,1],color="r")


plt.show()