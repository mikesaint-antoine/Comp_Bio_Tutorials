


## clear environment
rm(list=ls()) 



library(pheatmap)
# install.packages("pheatmap")



data <- read.table('data/gene_expression.csv', header=TRUE, row.names=1, sep=',')


sample_distance <- dist(t(data))


dist_mat <- as.matrix(sample_distance)

# pheatmap(dist_mat, clustering_distance_rows = sample_distance, clustering_distance_cols = sample_distance)


library(RColorBrewer)
# install.packages("RColorBrewer")


colors <- colorRampPalette( rev(brewer.pal(9,"Blues")))(255)



pheatmap(dist_mat, clustering_distance_rows = sample_distance, clustering_distance_cols = sample_distance, col=colors)


