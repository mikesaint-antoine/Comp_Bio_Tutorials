import numpy as np
import csv
import matplotlib
matplotlib.use('tkagg')
import matplotlib.pyplot as plt

import seaborn as sns


data = []
genes = []

first = True

with open("fake_gene_expression_data.csv") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

    for row in csv_reader:

        if first:
            sample_names = row[1:]
            first = False

        else:
            genes.append(row[0])
            data.append(row[1:])


data = np.array(data).astype(int)

# print(data)
# print(len(genes))
# print(len(sample_names))
# print(data.shape)


sns.set_context("paper", font_scale=0.3)


sns_plot = sns.clustermap(data, xticklabels=sample_names, yticklabels= genes)
sns_plot.savefig("heatmap.pdf")

plt.show()
