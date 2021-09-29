# 1
tcor <- data.frame(matrix(ncol=3,nrow=250000))
colnames(tcor) <- c('group','X','Y')
corl <- c()
for (i in 1:10000){
  bg <- 25*(i-1) + 1
  pg <- bg+24    # NO: [bg:bg+24]
  tcor$group[bg:pg] <- seq(from=i,to=i,length.out=25)
  tcor$X[bg:pg] <- rnorm(25)
  tcor$Y[bg:pg] <- rnorm(25)
  corl <- append(corl,cor(tcor$X[bg:pg],tcor$Y[bg:pg]))
}
plot(1:10000,corl,cex=0.1,xlab='Index',ylab='Correlation Coefficient')
 

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

# PCA analysis
df <- ep[3:dim(ep)[2]]
df.pca <- prcomp(df,center = TRUE,scale. = TRUE)
plot(df.pca$x,cex=0.5,main = 'PCA Result')

 


# 3
# Setting work path and Initialization
setwd('/Users/tianpei/BioComp_Homework/R_Homework/R3')
Hirsch <- read.table('Hirsch_Cancer_Cell.tab',header = TRUE)

# Normality Test
x <- t(Hirsch[2])
shapiro.test(sample(x,5000))

# Results:
# 	Shapiro-Wilk normality test

# data:  sample(x, 5000)
# W = 0.96412, p-value < 2.2e-16

# Normal QQ-plot
qqnorm(t(Hirsch[2]), cex=0.2)
qqline(t(Hirsch[2]), lwd=1,col=2)

# Same Distribution Test
y <- t(Hirsch[dim(Hirsch)[2]])
ks.test(x,y)

# Results:
#	Two-sample Kolmogorov-Smirnov test

# data:  x and y
# D = 0.0085908, p-value = 0.7887
# alternative hypothesis: two-sided

# Q-Q plot
qqplot(x,y,cex=0.5,col=2,xlab = 'hr0_D2',ylab = 'hr36_D3',main = 'Q-Q Plot')
par(new = TRUE)
lines(2:15,2:15,type = 'l',lwd = 2)
  

