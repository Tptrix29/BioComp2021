# 1
setwd("/Users/tianpei/BioComp_Homework/R_Homework/R4")
t <- read.table("Nucleosome_profile.xls")

pdf(file = '1.pdf', paper = 'a4')
plot(t$V2~t$V1, type = 'l', xlab = 'Relative Position', ylab = 'Location Signal', main = 'Plot 1')
dev.off()
 

# 2
setwd("/Users/tianpei/BioComp_Homework/R_Homework/R4")
t <- read.table('Hirsch_Cancer_Cell.tab', header = TRUE)
data <- t[,2:length(t)]

png(file = '2.png', width = 648 * 8, height = 648 * 8)
panel.cor <- function(x, y, ...){
  par(usr = c(0, 1, 0, 1))  
  txt <- as.character(format(cor(x, y), digits = 2))  
  text(0.5, 0.5, txt, cex = 6 * abs(cor(x, y)))  
}
pairs(data, upper.panel = panel.cor, pch = 0.005)
dev.off()
 


# 3
setwd("/Users/tianpei/BioComp_Homework/R_Homework/R4")
t <- read.table('Hirsch_Cancer_Cell.tab', header = TRUE)
data <- t[, 2:length(t)]

png(file = '3.png')
corr <- cor(data)
out.dist=dist(corr,method="euclidean") 
out.hclust=hclust(out.dist,method="complete")
plot(out.hclust, xlab = "Column Label", sub = "")    
dev.off()
 

# 4
# Data preparation
# R3 T2
# Initialization
setwd('/Users/tianpei/BioComp_Homework/R_Homework/R3/filtered_gene_bc_matrices')
info <- read.table('matrix.mtx',skip=3)
gene <- read.table("genes.tsv")
cell <- read.table('barcodes.tsv')
ep <- data.frame(matrix(ncol=dim(cell)[1],nrow=dim(gene)[1]))
colnames(gene) <- c('ID','Gene')
colnames(ep)<-t(cell)[1,]

# Sparse Matrix transfer to Expression Matrix
ep <- data.frame(matrix(ncol=dim(cell)[1], nrow=dim(gene)[1]))
for (i in 1:dim(info)[1]){
  ep[info[i,1], info[i,2]] <- info[i,3]
  # print(i)
}

# NA processing 
ep[is.na(ep)] <- 0

# Information Combination
ep <- cbind(gene,ep)

# 4.1
setwd("/Users/tianpei/BioComp_Homework/R_Homework/R4")
new_ep <- ep[grep('MT-', ep$Gene, invert = TRUE),]
new_ep <- new_ep[apply(new_ep[,3:dim(new_ep)[2]],1,sum) >= 3,]

# > dim(new_ep)
# [1] 13753  2702
 

# 4.2
cnd <- apply(new_ep[,3:dim(new_ep)[2]],2,sum)
nep <- new_ep[,3:dim(new_ep)[2]][, cnd >= 1000 & cnd <= 2500]
rm(cnd)
nep <- cbind(new_ep[,1:2],nep)

# > dim(nep)
# [1] 13753  1652
 

# 4.3
png(file = '4.png')
mat <- as.matrix((scale(nep[,3:dim(nep)[2]]))) 
heatmap(mat, scale="row")
dev.off()

 



