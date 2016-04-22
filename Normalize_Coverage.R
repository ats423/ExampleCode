my_table <- read.table("/home/alexandra/hw7/chr_13_depth.sample_interval_summary", sep="\t", header=T)
data <- interval_summary[,grep("mean_cvg", colnames(my_table))]
data2 <- apply(data, 2, function(x) log2(x/median(x,na.rm=T)))
