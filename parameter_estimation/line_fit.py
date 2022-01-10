import matplotlib.pyplot as plt
import numpy as np
import random
import csv
import scipy.optimize




heights = []
skills = []

with open("basketball_skills.csv") as file:

    reader = csv.reader(file, delimiter=',')

    # skip header
    next(reader)

    for row in reader:
        heights.append(float(row[0]))
        skills.append(float(row[1]))



def loss_function(params, heights, skills):

    m = params[0]
    b = params[1]

    loss = 0

    for i in range(len(heights)):
        predicted_skills = m * heights[i] + b

        res = (predicted_skills - skills[i])**2

        loss += res

    return(loss)

#[m,b]
# params0 = np.array([0,0])
# minimum = scipy.optimize.fmin(loss_function,params0, args=(heights, skills))
#
# print(minimum)



for counter in range(100000):
    test_m = random.uniform(0,20)
    test_b = random.uniform(-100,100)

    current_params = [test_m, test_b]

    current_loss = loss_function(current_params, heights, skills)

    if counter == 0:
        best_loss = current_loss
        best_params = current_params
    else:
        if current_loss < best_loss:
            best_loss = current_loss
            best_params = current_params


print(best_loss)
print(best_params)


m_fit = best_params[0]
b_fit = best_params[1]


x = []
y = []

def line(x,m,b):
    return( m*x + b)


for i in range(40,90):
    x.append(i)
    y.append(line(i,m_fit,b_fit))


plt.plot(x,y,color="red",linewidth=3)
plt.scatter(heights,skills, s=10, color="black")
plt.xlabel("Height (inches)",fontsize=16)
plt.ylabel("Basketball Skills", fontsize=16)

plt.show()
