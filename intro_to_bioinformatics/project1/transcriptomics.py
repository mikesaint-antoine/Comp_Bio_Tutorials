import numpy as np
import csv
import random
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind, ks_2samp
import seaborn as sns

# data link: https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE150910
# paper link: https://pmc.ncbi.nlm.nih.gov/articles/PMC7667907/




genes = []
data = []

with open("data/GSE150910_gene-level_count_file.csv") as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        
        genes.append(row[0])
        data.append(row[1:])


samples = data[0]
data = data[1:]
genes = genes[1:]


data = np.array(data).astype(float)
genes = np.array(genes)
samples = np.array(samples)



labels = []

for i in range(len(samples)):
    tmp = samples[i].split("_")
    labels.append(tmp[0])
    
labels = np.array(labels)




data = data[:,labels != "chp"]
samples = samples[labels != "chp"]
labels = labels[labels != "chp"]


# counts-per-million (CPM) normalization
for j in range(data.shape[1]):
    column_sum = sum(data[:,j])
    
    data[:,j] = data[:,j] / column_sum * 1000000


# filtering out low expression genes
mean_CPM_control = data[:,labels == "control"].mean(axis=1)
mean_CPM_ipf = data[:,labels == "ipf"].mean(axis=1)

to_keep = (mean_CPM_ipf >= 5) | (mean_CPM_control >= 5)

data = data[to_keep,:]
genes = genes[to_keep]



# getting p-value and log2FC, now for every gene

p_values = []
log2_FCs = []

epsilon = 1  # small constant to avoid division by zero

for i in range(data.shape[0]):
    
    control = data[i, labels == "control"]
    ipf = data[i, labels == "ipf"]

    # perform ks-test
    ks_statistic, p_value = ks_2samp(control, ipf)

    # save p_value for this gene
    p_values.append(p_value)


    # calculate means for each condition
    control_mean = np.mean(control)
    ipf_mean = np.mean(ipf)

    # calculate log2(fold change), adding epsilon to avoid division by 0
    FC = (ipf_mean + epsilon) / (control_mean + epsilon)
    log2_FC = np.log2(FC)
    
    # save log2_FC for this gene
    log2_FCs.append(log2_FC)


# cast results to numpy arrays
p_values = np.array(p_values)
log2_FCs = np.array(log2_FCs)


p_values_bonf = p_values * len(genes)


to_keep = (p_values_bonf <= 0.01) & (np.abs(log2_FCs) >= 2)

sig_genes = genes[to_keep]
sig_log2_FCs = log2_FCs[to_keep]
sig_p_values_bonf = p_values_bonf[to_keep]
sig_data = data[to_keep, :]


print(f"Number of DEGs: {len(sig_genes)}")
print(f"Total number of genes: {len(genes)}")
print(f"DEG percentage: {len(sig_genes) / len(genes) * 100}")
print()
print(f"Number of upregulated DEGs: {np.sum(sig_log2_FCs>0)}")
print(f"Number of downregulated DEGs: {np.sum(sig_log2_FCs<0)}")


# saving upregulated DEGs         
output_file = "output/upregulated_DEGs.csv"
with open(output_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    
    writer.writerow(["gene", "p_value", "log2_FC"])

    for i in range(len(sig_genes)):
        if sig_log2_FCs[i] > 0:
            writer.writerow([sig_genes[i], sig_p_values_bonf[i], sig_log2_FCs[i]])


# saving downregulated DEGs         
output_file = "output/downregulated_DEGs.csv"
with open(output_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    
    writer.writerow(["gene", "p_value", "log2_FC"])

    for i in range(len(sig_genes)):
        if sig_log2_FCs[i] < 0:
            writer.writerow([sig_genes[i], sig_p_values_bonf[i], sig_log2_FCs[i]])


sig_data_log2fc = np.zeros_like(sig_data)



epsilon = 1  # small constant to avoid division by zero


for i in range(len(sig_genes)):
    
    control_mean =  np.mean(sig_data[i,labels == "control"])
    
    sig_data_log2fc[i,:] = np.log2((sig_data[i,:]+epsilon) / (control_mean +epsilon))
    


sns_plot = sns.clustermap(sig_data_log2fc, xticklabels=samples, yticklabels= sig_genes, cmap="coolwarm", vmin=-6, vmax=6)

# changing font sizes for x and y labels
sns_plot.ax_heatmap.set_xticklabels(sns_plot.ax_heatmap.get_xmajorticklabels(), fontsize=2)
sns_plot.ax_heatmap.set_yticklabels(sns_plot.ax_heatmap.get_ymajorticklabels(), fontsize=2)


sns_plot.savefig("output/heatmap.pdf")

plt.show()






## expression bar plot

gene_to_plot = "POSTN"

control_expression = data[genes==gene_to_plot, labels == "control"]
ipf_expression = data[genes==gene_to_plot, labels == "ipf"]

control_mean = np.mean(control_expression)
control_sem = np.std(control_expression) / np.sqrt(len(control_expression))
ipf_mean = np.mean(ipf_expression)
ipf_sem = np.std(ipf_expression) / np.sqrt(len(ipf_expression))

conditions = ['Control', 'IPF']
means = [control_mean, ipf_mean]
errors = [control_sem, ipf_sem]

plt.bar(conditions, means, yerr=errors, capsize=5, color=['blue', 'red'])
plt.ylabel('Expression Level')
plt.title(f'{gene_to_plot} Expression')
# plt.savefig(f"output/{gene_to_plot}_expression_bar.pdf")
plt.show()



# expression scatter plot

gene_to_plot = "POSTN"

control_expression = data[genes == gene_to_plot, labels == "control"]
ipf_expression = data[genes == gene_to_plot, labels == "ipf"]

control_mean = np.mean(control_expression)
control_sem = np.std(control_expression) / np.sqrt(len(control_expression))
ipf_mean = np.mean(ipf_expression)
ipf_sem = np.std(ipf_expression) / np.sqrt(len(ipf_expression))

def add_jitter(values, jitter_amount=0.05):
    return values + np.random.uniform(-jitter_amount, jitter_amount, size=values.shape)

control_x = add_jitter(np.ones_like(control_expression) * 1)
ipf_x = add_jitter(np.ones_like(ipf_expression) * 2)

plt.scatter(control_x, control_expression, color='blue', label='Control', s=10)  # smaller dots with s=10
plt.scatter(ipf_x, ipf_expression, color='red', label='IPF', s=10)  # smaller dots with s=10

plt.errorbar(1, control_mean, yerr=control_sem, fmt='o', color='blue', capsize=5)
plt.errorbar(2, ipf_mean, yerr=ipf_sem, fmt='o', color='red', capsize=5)

plt.xticks([1, 2], ['Control', 'IPF'])

plt.ylabel('Expression Level')
plt.title(f'{gene_to_plot} Expression')
plt.legend()

# plt.savefig(f"output/{gene_to_plot}_expression_scatter.pdf")
plt.show()




# DEG expression correlation

correlation_matrix = np.corrcoef(sig_data)

sns_plot = sns.clustermap(correlation_matrix, 
                          xticklabels=sig_genes, 
                          yticklabels=sig_genes, 
                          cmap="coolwarm", 
                          annot=False, 
                          linewidths=.5, 
                          figsize=(12, 10))

sns_plot.ax_heatmap.set_xticklabels(sns_plot.ax_heatmap.get_xmajorticklabels(), fontsize=2)
sns_plot.ax_heatmap.set_yticklabels(sns_plot.ax_heatmap.get_ymajorticklabels(), fontsize=2)

# sns_plot.savefig("output/degs_correlation_heatmap.pdf")
plt.show()
