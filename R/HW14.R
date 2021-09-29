# 1
setwd("/Users/tianpei/BioComp_Homework/R_Homework/R5")
Hirsch <- read.table('Hirsch_Cancer_Cell.tab', header = TRUE)
exp <- Hirsch[, c(2,20)]

fun_A <- function(exp, x1, x2){
  log2(exp[x1] * exp[x2]) / 2
}

fun_M <- function(exp, x1, x2){
  log2(exp[x1] / exp[x2])
}

exp['logFC'] <- apply(exp, 1, fun_M, x1 = colnames(exp)[1], x2 = colnames(exp)[2])
exp['FPKM'] <- apply(exp, 1, fun_A, x1 = colnames(exp)[1], x2 = colnames(exp)[2])
# Plot as PDF
pdf(file = '1.pdf', paper = 'a4')
FC <- 0.5
exp['cat'] <- ifelse(exp$logFC > FC, 'Up', ifelse(exp$logFC < -FC, 'Down', 'Normal'))
label <- factor(exp$cat)
plot(exp$FPKM, exp$logFC, xlab = 'FPKM', ylab = 'logFC', main = 'MA Plot', 
     cex = c(0.8, 0.5, 0.8)[label], col = c('blue', 'grey', 'red')[label], 
     ylim = c(-1,1))
legend(x="topright", legend = levels(label), col=c('blue', 'grey', 'red'), pch=1)
dev.off()
 

# 2
setwd("/Users/tianpei/BioComp_Homework/R_Homework/R5")
t <- read.csv('transcript_count_matrix.csv', header = TRUE)
gene_len <- read.table('gene_length.txt', row.names = 1)
colnames(gene_len) <- 'len'
# Character Analysis to Get Gene ID
get_id <- function(t, id){
    strsplit(t[id], "[.]")[[1]][1]
}
t["ID"] <- apply(t, 1, get_id, id = 'transcript_id')
# Get the length of Gene
get_len <- function(t, ID, len_data){
  len_data[t[ID], 1]
}
t["len"] <- apply(t, 1, get_len, ID = 'ID', len_data = gene_len)

# RPKM
col <- 'mcm3l_1k_20181022_ensGene'
n <- sum(t['mcm3l_1k_20181022_ensGene']) / 1000000
RPKM <- function(t, col_name, total){
  as.integer(t[col_name]) / (as.integer(t['len']) * total / 1000)
}
apply(t, 1, RPKM, col_name = col, total = n)
	
# TPM
col <- 'mcm3l_1k_20181022_ensGene'
PM <- function(t, col_name){
  as.integer(t[col_name]) * as.integer(t['len']) 
}
total <- sum(apply(t, 1, PM, col_name = col)) / 1000000
TPM <- function(t, col_name, N){
  as.integer(t[col_name]) * as.integer(t['len']) / N
}
apply(t, 1, TPM, col_name = col, N = total)


# 3
setwd("/Users/tianpei/BioComp_Homework/R_Homework/R5")
df <- read.table('NAR_2020.tab', header = TRUE, row.names = 1)
attach(df)
m <- lm(expression~H3K27me3_promoter+H3K36me3_genebody+H3K4me3_promoter)
summary(m)
# Call:
# lm(formula = expression ~ H3K27me3_promoter + H3K36me3_genebody + 
#     H3K4me3_promoter)
#
# Residuals:
#      Min       1Q   Median       3Q      Max 
# -16.2011  -1.0046  -0.3405   0.9135   8.8296 
#
# Coefficients:
#                    Estimate Std. Error t value Pr(>|t|)    
# (Intercept)        3.984869   0.024163  164.92   <2e-16 ***
# H3K27me3_promoter -0.767078   0.026532  -28.91   <2e-16 ***
# H3K36me3_genebody  1.559793   0.022163   70.38   <2e-16 ***
# H3K4me3_promoter   0.116524   0.003167   36.79   <2e-16 ***
# ---
# Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1
# 
# Residual standard error: 1.714 on 20494 degrees of freedom
# Multiple R-squared:  0.5438,	Adjusted R-squared:  0.5437 
# F-statistic:  8143 on 3 and 20494 DF,  p-value: < 2.2e-16

# Plot Result
plot(m, cex = 0.5)





