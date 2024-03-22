


## clear environment
rm(list=ls()) 

# dataset
# https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE150910




data <- read.table('GSE150910_gene-level_count_file.csv', header=TRUE, sep=',', row.names=1)


samples <- colnames(data)
genes <- rownames(data)


classes <- c()

for(sample in samples){
  
  tmp <- unlist(strsplit(sample,"_"))
  classes <- append(classes, tmp[1])
  
}


filtered_data <- data[, classes %in% c("control","ipf") ]
filtered_classes <- classes[classes %in% c("control","ipf") ]


saveRDS(filtered_data, file = "rds_objects/filtered_data.RDS")
saveRDS(filtered_classes, file = "rds_objects/filtered_classes.RDS")



# filtered_data <- readRDS("rds_objects/filtered_data.RDS")
# filtered_classes <- readRDS("rds_objects/filtered_classes.RDS")





