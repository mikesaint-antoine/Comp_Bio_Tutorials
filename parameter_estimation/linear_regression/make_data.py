import matplotlib.pyplot as plt
import random
import csv
import numpy as np

heights = []
for count in range(750):
    heights.append(random.uniform(40,90))



def basketball_skills(height,m,b):
    skill = m*height + b + np.random.normal(loc=0.0, scale=7.0,)
    return(skill)




skills = []

####################
# TRUE PARAMS

m = 2
b = 10

####################


for height in heights:
    skill = basketball_skills(height, m,b)
    skills.append(skill)


heights.append(72)

skills.append(75)



plt.scatter(heights,skills, s=10, color="black")
plt.xlabel("Height (inches)",fontsize=16)
plt.ylabel("Basketball Skills", fontsize=16)

plt.show()





f = open('basketball_skills.csv', "w")

f.write("height_inches,basketball_skills\n")

for i in range(len(heights)):
    f.write("%s,%s\n" % (heights[i],skills[i]))

f.close()
