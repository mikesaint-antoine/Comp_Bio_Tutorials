## clear environment
rm(list=ls()) 

# dataset
# https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE150910


# used to manage Bioconductor packages
# install.packages("BiocManager")
# BiocManager::install("DESeq2")

library(DESeq2)


data <- readRDS("rds_objects/filtered_data.RDS")
classes <- readRDS("rds_objects/filtered_classes.RDS")



samples_info <- data.frame(
  
  condition = factor(classes, levels = c("control","ipf"))
  
  
)


rownames(samples_info) <- colnames(data)



dds <- DESeqDataSetFromMatrix(countData = data,
                              colData = samples_info,
                              design = ~ condition)



dds <- DESeq(dds)



results <- results(dds)


# head(results[order(results$padj),])



significance_threshold <- 0.01

significant_results <- results[which(results$padj < significance_threshold), ]


upregulated <- rownames(significant_results[significant_results$log2FoldChange > 0,])
downregulated <- rownames(significant_results[significant_results$log2FoldChange < 0,])





