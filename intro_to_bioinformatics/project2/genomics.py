import csv
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm

# random seed for reproducibility
np.random.seed(42)


##############################################################################################################
##############################################################################################################
##############################################################################################################
# STEP 1: Logistic Regression Review (OPTIONAL)

# making test data for one SNP

N = 200

p_control = 0.2
p_case = 0.8

snp_control = np.random.choice([0,1,2], size=int(N/2), p=[(1-p_control)**2, 2*p_control*(1-p_control), p_control**2])
snp_case = np.random.choice([0,1,2], size=int(N/2), p=[(1-p_case )**2, 2*p_case *(1-p_case ), p_case**2])

# combine
snp = np.concatenate([snp_control, snp_case])
labels = np.array([0]*100 + [1]*100)



print("Genotype shape:", snp.shape)
print("First couple genotypes:", snp[0:10])
print("Unique genotype values:", np.unique(snp))
print()
print("Labels shape:", labels.shape)
print("First couple lables:", labels[0:10])
print("Unique lable values:", np.unique(labels))



plt.figure()
# add small random noise for display
x_jitter = snp + np.random.normal(0, 0.05, size=N)
plt.scatter(x_jitter, labels, alpha=0.6)
plt.yticks([0,1], ["0 (Control)", "1 (Case)"])
plt.xticks([0,1,2], ["0 (ref,ref)", "1 (ref,alt)","2 (alt,alt)"])

plt.xlabel("Genotype")
plt.ylabel("Status")
plt.show()





def logistic(x, beta_0, beta_1):
    return 1 / (1 + np.exp(-(beta_0 + beta_1 * x)))

x_vals = np.linspace(0, 2, 300)

plt.figure()
# three example parameter sets
for b0, b1 in [(0, 1), (-2, 2), (2, -1)]:
    plt.plot(x_vals, logistic(x_vals, b0, b1), label=f"beta_0={b0}, beta_1={b1}")
plt.scatter([], [], label="↑ examples", alpha=0)  # placeholder for legend
plt.xlabel("Genotype")
plt.ylabel("Predicted zombie-probability")

plt.yticks([0,1], ["0", "1"])
plt.xticks([0,1,2], ["0 (ref,ref)", "1 (ref,alt)","2 (alt,alt)"])
plt.title("Example Logistic Curves\n(varying beta_0 and beta_1)")
plt.legend()
plt.show()




# add constant column for intercept
X = sm.add_constant(snp)
model = sm.Logit(labels, X)
result = model.fit(disp=False)





fit_beta_0, fit_beta_1 = result.params

print(f"Fit beta_0: {round(fit_beta_0,3)}")
print(f"Fit beta_1: {round(fit_beta_1,3)}")





plt.figure()
# scatter raw data
plt.scatter(x_jitter, labels, alpha=0.6)

# logistic curve using fitted params
x_plot = np.linspace(0, 2, 200)
y_plot = logistic(x_plot, fit_beta_0, fit_beta_1)
plt.plot(x_plot, y_plot, linewidth=2)

plt.yticks([0,1], ["Control", "Case"])
plt.xlabel("Genotype")
plt.ylabel("Status / Predicted probability")
plt.yticks([0,1], ["0 (Normal)", "1 (Zombie)"])
plt.xticks([0,1,2], ["0 (ref,ref)", "1 (ref,alt)","2 (alt,alt)"])

plt.show()




prob_0 = logistic(0, fit_beta_0, fit_beta_1)
print(f"Zombie-probability, genotype 0 (ref,ref) = {round(prob_0,3)}")
print()

prob_1 = logistic(1, fit_beta_0, fit_beta_1)
print(f"Zombie-probability, genotype 1 (ref,alt) = {round(prob_1,3)}")
print()

prob_2 = logistic(2, fit_beta_0, fit_beta_1)
print(f"Zombie-probability, genotype 2 (alt,alt) = {round(prob_2,3)}")
print()








p_value = result.pvalues[1]
print(p_value)






# binary smoker status: ~30% smokers
smoker_status = np.random.binomial(1, 0.3, size=len(labels))

# age in years: mean 50, sd 10
age = np.random.normal(loc=50, scale=10, size=N).astype(int)

X = np.column_stack((snp, smoker_status, age))
X = sm.add_constant(X)  
# columns: constant, snp, smoker, age

model = sm.Logit(labels, X)
result = model.fit(disp=False)

print(result.summary())




##############################################################################################################
##############################################################################################################
##############################################################################################################
# STEP 2: Reading in the Data




snp_info = []
data = []
with open("data/example_data.csv") as csvfile:
    reader = csv.reader(csvfile, delimiter=',')

    for row in reader:

        snp_info.append(row[0:3])
        data.append(row[3:])





snp_header = snp_info[0]
snp_info = snp_info[1:]

samples = data[0]
data = data[1:]




snp_info = np.array(snp_info)
data = np.array(data).astype(int)

snp_header = np.array(snp_header)
samples = np.array(samples)





print(snp_info.shape)
print(data.shape)
print()
print(snp_header.shape)
print(samples.shape)






print("snp_header:")
print(snp_header)
print()

print("samples:")
print(samples[0:3])
print()

print("snp_info:")
print(snp_info[0:5])
print()

print("data:")
print(data[0:5,0:3])
print()




labels = []

for i in range(len(samples)):
    tmp = samples[i].split("_")
    labels.append(tmp[0])
    
labels = np.array(labels)




print(labels[0:5])

print(np.unique(labels))




##############################################################################################################
##############################################################################################################
##############################################################################################################
# STEP 3: Filtering SNPs



first_snp = data[0,:]

print(first_snp)




total_alleles_per_snp = len(samples)*2

print(total_alleles_per_snp)




ref_allele_count = 2 * np.sum(first_snp == 0) + np.sum(first_snp == 1)
# purposely writing this in a mathematically inefficient way to communicate the point
# could just be total_alleles_per_snp - np.sum(first_snp)

print(ref_allele_count)





alt_allele_count = 2 * np.sum(first_snp == 2) + np.sum(first_snp == 1)
# purposely writing this in a mathematically inefficient way to communicate the point
# could just be np.sum(first_snp)

print(alt_allele_count)




maf = min(ref_allele_count, alt_allele_count) / total_alleles_per_snp

print(maf)





maf_threshold = 0.05
total_alleles_per_snp = len(samples)*2


to_keep = []

for i in range(data.shape[0]):

    # again writing these in a mathematically inefficient way to hopefully make it clear what we're counting
    ref_allele_count = 2 * np.sum(data[i,:] == 0) + np.sum(data[i,:] == 1)
    alt_allele_count = 2 * np.sum(data[i,:] == 2) + np.sum(data[i,:] == 1)

    maf = min(ref_allele_count, alt_allele_count) / total_alleles_per_snp

    if maf >= maf_threshold:
        to_keep.append(True)
    else:
        to_keep.append(False)




to_keep = np.array(to_keep)

filtered_snp_info = snp_info[to_keep,:]
filtered_data = data[to_keep,:]


print("shape checks:")
print(filtered_snp_info.shape)
print(filtered_data.shape)
print()

print(f"Percent kept: {filtered_data.shape[0] / data.shape[0] * 100}")



##############################################################################################################
##############################################################################################################
##############################################################################################################
# STEP 4: GWAS Analysis



encoded_labels = np.where(labels == "zombie", 1, 0)

print(encoded_labels)


first_snp = filtered_data[0, :]

print(first_snp)


X = sm.add_constant(first_snp)
result = sm.Logit(encoded_labels, X).fit(disp=False)

print(result.summary())




p_value = result.pvalues[1] # p‑value for the SNP term

print(p_value)





p_values = []

for i in range(filtered_data.shape[0]):
    
    snp_genotypes = filtered_data[i, :]

    X = sm.add_constant(snp_genotypes.astype(float))
    result = sm.Logit(encoded_labels, X).fit(disp=False)

    if result.mle_retvals["converged"]:
        p_value = result.pvalues[1]
        p_values.append(p_value)

    else:
        p_value = 1.0 # model didn't converge on an answer, so p_value isn't reliable. we'll assign the highest (least-significant) p_value
        p_values.append(p_value)




p_values = np.array(p_values)



print(np.sum(np.isnan(p_values))) # should be 0
print(p_values[0:5])




p_values_bonf = p_values * len(p_values)




print(filtered_snp_info[p_values_bonf <= 0.05, ])







##############################################################################################################
##############################################################################################################
##############################################################################################################
# STEP 5: Manhattan Plot


filtered_snp_chromosomes = []
filtered_snp_positions = []


for i in range(filtered_snp_info.shape[0]):
    
    snp_position = filtered_snp_info[i,0]
    
    chromosome, position = snp_position.split(":")
    
    chromosome = chromosome.replace('chr', '')
    
    chromosome = int(chromosome)
    position = int(position)
    
    
    filtered_snp_chromosomes.append(chromosome)
    filtered_snp_positions.append(position)
    
    
filtered_snp_chromosomes = np.array(filtered_snp_chromosomes)
filtered_snp_positions = np.array(filtered_snp_positions)




neg_log_p_values = -np.log10(p_values)







# Create a DataFrame-like structure using NumPy
snp_data = np.column_stack((filtered_snp_chromosomes, filtered_snp_positions, neg_log_p_values))

# Sort the data by chromosome and position
snp_data = snp_data[np.lexsort((snp_data[:, 1], snp_data[:, 0]))]

# Compute cumulative positions
cumulative_positions = np.zeros_like(filtered_snp_positions)
chromosome_offsets = {}
midpoints = []

current_offset = 0
for chromosome in np.unique(filtered_snp_chromosomes):
    chrom_mask = filtered_snp_chromosomes == chromosome
    chromosome_offsets[chromosome] = current_offset
    cumulative_positions[chrom_mask] = filtered_snp_positions[chrom_mask] + current_offset
    midpoints.append((current_offset + np.max(cumulative_positions[chrom_mask])) / 2)
    current_offset += np.max(filtered_snp_positions[chrom_mask]) + 1  # Add a buffer between chromosomes

# Prepare the Manhattan plot
plt.figure(figsize=(12, 6))

# Define colors for different chromosomes
colors = ['#1f77b4', '#ff7f0e']

# Plot each chromosome with alternating colors and smaller dots
dot_size = 10  # Adjust this value to change the size of the dots
current_chromosome = 1
for chromosome in np.unique(snp_data[:, 0]):
    chrom_mask = snp_data[:, 0] == chromosome
    plt.scatter(cumulative_positions[chrom_mask], snp_data[chrom_mask, 2], c=colors[current_chromosome % 2], s=dot_size, label=f'Chromosome {chromosome}')
    current_chromosome += 1

# Add chromosome labels at midpoints
plt.xticks(midpoints, np.unique(filtered_snp_chromosomes))

# Add significance line
sig_thresh = -np.log10(0.05/filtered_data.shape[0])
plt.axhline(y=sig_thresh,
            color='grey',
            linestyle='--',
            linewidth=1,
            alpha=0.4)

# Add labels and title
plt.xlabel('Chromosome')
plt.ylabel('-log10(p-value)')
plt.title('Manhattan Plot of GWAS Results')
# plt.legend()

# Show the plot
plt.savefig("output/manhattan_plot.pdf")

plt.show()



##############################################################################################################
##############################################################################################################
##############################################################################################################
# STEP 6: More Checks


snp_id_to_check = "chr1:221240797"

snp_to_check = filtered_data[filtered_snp_info[:,0] == snp_id_to_check, :].flatten()

print(filtered_snp_info[filtered_snp_info[:,0] == snp_id_to_check, :])
print(snp_to_check)




snp_to_check_NORMAL = snp_to_check[encoded_labels==0]
snp_to_check_ZOMBIE = snp_to_check[encoded_labels==1]

# out of all the people with genotype 0 (ref,ref), what fraction were zombies?
zombie_frac_0 = np.sum(snp_to_check_ZOMBIE==0) / (np.sum(snp_to_check_ZOMBIE==0) + np.sum(snp_to_check_NORMAL==0))
print(f"{round(zombie_frac_0*100,3)}% of people with genotype 0 (ref,ref) for SNP {snp_id_to_check} were zombies.")

# out of all the people with genotype 1 (ref,alt), what fraction were zombies?
zombie_frac_1 = np.sum(snp_to_check_ZOMBIE==1) / (np.sum(snp_to_check_ZOMBIE==1) + np.sum(snp_to_check_NORMAL==1))
print(f"{round(zombie_frac_1*100,3)}% of people with genotype 1 (ref,alt) for SNP {snp_id_to_check} were zombies.")

# out of all the people with genotype 2 (alt,alt), what fraction were zombies?
zombie_frac_2 = np.sum(snp_to_check_ZOMBIE==2) / (np.sum(snp_to_check_ZOMBIE==2) + np.sum(snp_to_check_NORMAL==2))
print(f"{round(zombie_frac_2*100,3)}% of people with genotype 2 (alt,alt) for SNP {snp_id_to_check} were zombies.")





plt.figure()
# add small random noise for display
x_jitter = snp_to_check + np.random.normal(0, 0.05, size=N)
plt.scatter(x_jitter, encoded_labels, alpha=0.6)
plt.yticks([0,1], ["0 (Normal)", "1 (Zombie)"])
plt.xticks([0,1,2], ["0 (ref,ref)", "1 (ref,alt)","2 (alt,alt)"])

plt.xlabel("Genotype")
plt.ylabel("Status")
plt.title(snp_id_to_check)
plt.show()


# add constant column for intercept
X = sm.add_constant(snp_to_check)
model = sm.Logit(encoded_labels, X)
result = model.fit(disp=False)

print(result.summary())
b0_hat, b1_hat = result.params
print(f"Fitted intercept b0 = {b0_hat:.3f}, slope b1 = {b1_hat:.3f}")




plt.figure()
# scatter raw data
plt.scatter(x_jitter, encoded_labels, alpha=0.6)

# logistic curve using fitted params
x_plot = np.linspace(-0.5, 2.5, 200)
y_plot = logistic(x_plot, b0_hat, b1_hat)
plt.plot(x_plot, y_plot, linewidth=2)

plt.yticks([0,1], ["Control", "Case"])
plt.xlabel("Genotype")
plt.ylabel("Status")
plt.yticks([0,1], ["0 (Normal)", "1 (Zombie)"])
plt.xticks([0,1,2], ["0 (ref,ref)", "1 (ref,alt)","2 (alt,alt)"])
plt.title(snp_id_to_check)
plt.show()