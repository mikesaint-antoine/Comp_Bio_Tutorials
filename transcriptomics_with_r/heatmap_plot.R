## clear environment
rm(list=ls()) 

# dataset
# https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE150910




################################################################################################################################################
################################################################################################################################################
################################################################################################################################################
################################################################################################################################################
################################################################################################################################################
###############
# PREVIOUS CODE
###############


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





################################################################################################################################################
################################################################################################################################################
################################################################################################################################################
################################################################################################################################################
################################################################################################################################################
###############
# NEW CODE
###############


# install.packages("pheatmap")
library(pheatmap)


N <- 100

top_genes <- head(rownames(significant_results[order(significant_results$padj),]), N)



norm_counts <- counts(dds, normalized=TRUE)

heatmap_data <- norm_counts[top_genes, ]



pdf("plots/heatmap_plot.pdf", width = 10, height = 8)

my_colors <- colorRampPalette(c("blue", "white", "red"))(50)

annotation_colors <- list(
  condition = c(control = "yellow", ipf = "orange") 
)


pheatmap(heatmap_data, scale = "row", clustering_distance_rows = "euclidean", clustering_distance_cols = "euclidean",
         clustering_method = "complete", annotation_col = samples_info,annotation_colors = annotation_colors,color = my_colors,fontsize_row = 6,fontsize_col = 4)


dev.off()



