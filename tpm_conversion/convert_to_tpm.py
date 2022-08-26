import numpy as np
import csv
import pandas as pd




## read in data


length_dict = {}
with open("lengths.csv") as csvfile:

    reader = csv.reader(csvfile, delimiter=',')

    for row in reader:
        length_dict[row[0]] = float(row[1])



data = []
with open("raw_data.csv") as csvfile:

    reader = csv.reader(csvfile, delimiter=',')


    for row in reader:
        data.append(row)

genes = data[0]

data = data[1:]

data = np.array(data).astype(float)


print(data)


## TPM steps
## Step 1: Normalize for gene length (kilobases) -> this gives Reads Per Kilobase (RPK)
## Step 2: Normalize for sequencing depth (divide by total RPK)



## Step 1


rpk = np.zeros(shape=(data.shape[0],data.shape[1]))


for i in range(data.shape[0]):
    for j in range(data.shape[1]):
        gene_length = length_dict[genes[j]]

        gene_length_in_kilo = gene_length/1000

        rpk[i,j] = data[i,j] / gene_length_in_kilo



## Step 2
tpm = np.zeros(shape=(data.shape[0],data.shape[1]))

for i in range(rpk.shape[0]):

    total_rpk = np.sum(rpk[i,:])

    scaled_total_rpk = total_rpk / 1000000

    for j in range(rpk.shape[1]):

        if scaled_total_rpk != 0:
            tpm[i,j] = rpk[i,j] / scaled_total_rpk
        else:
            tpm[i,j] = rpk[i,j]  # going to be 0



pd.DataFrame(tpm).to_csv("tpm.csv",header=genes,index=False)






