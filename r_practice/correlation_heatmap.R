


## clear environment
rm(list=ls()) 



library(pheatmap)
# install.packages("pheatmap")

data <- read.table('data/gene_expression.csv', header=TRUE, row.names=1, sep=',')


data <- t(data)

cor_mat <- cor(data)


pheatmap(cor_mat, fontsize_row=10, fontsize_col = 10, main="Gene Expression Correlations")


library(RColorBrewer)
# install.packages("RColorBrewer)

colors <- colorRampPalette(brewer.pal(9, "Blues"))(255)



pheatmap(cor_mat,col=colors, fontsize_row=10, fontsize_col = 10, main="Gene Expression Correlations")








