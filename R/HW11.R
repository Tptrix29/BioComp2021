# 1.1
setwd('/Users/tianpei/BioComp_Homework/R_Homework/R2')
Hirsch <- read.table("Hirsch_Cancer_Cell.tab", row.names=1, header=TRUE)
quantile(apply(Hirsch,1,sd),probs = c(0,0.999,1))
 
  
# 1.2
time_list <- paste('hr',c(0,1,2,4,8,12,16,24,36),sep = '')
newdf <- data.frame(matrix(ncol=9,nrow=11524))
names(newdf) <- time_list
for (i in 1:length(time_list)) {
  pt = paste(time_list[i],'_',sep='')
  col <- grep(pt, colnames(Hirsch))
  newdf[i] <- data.frame(apply(Hirsch[col],1,mean))
}
row.names(newdf) <- row.names(Hirsch)
 

# 2 
incr <- data.frame(matrix(ncol=9,nrow=0))
decr <- data.frame(matrix(ncol=9,nrow=0))
colnames(incr) <- colnames(newdf)
colnames(decr) <- colnames(newdf)

re <- data.frame(t(as.matrix(apply(newdf, 1, diff))))

for (i in 1:dim(re)[1]) {
  cnd <- levels(factor(re[i,] > 0))
  if (("TRUE" %in% cnd) && (length(cnd) == 1)){
    incr <- rbind(incr, newdf[i,])
  }else if (("FALSE" %in% cnd) && (length(cnd) == 1)){
    decr <- rbind(decr, newdf[i,])
  }else{
    next
  } 
}


# 3.1
setwd('/Users/tianpei/BioComp_Homework/R_Homework/R2')
CpG <- read.table("WT_CpG.txt", header=TRUE)
newCpG <- CpG[which(CpG$freqC >= CpG$freqT), ]
 

# 3.2
# process refGene dataset to get promoter region
refGene <- read.table("mm9.main.refGene.txt", header = TRUE)
ref1 <- refGene[which(refGene$strand == '+'),]
ref2 <- refGene[which(refGene$strand == '-'),]

for (i in 1:dim(ref1)[1]){
  ref1[i,'promStart'] <- ref1[i,]$txStart - 2000
  ref1[i,'promEnd'] <- ref1[i,]$txStart + 2000
}

for (i in 1:dim(ref2)[1]){
  ref2[i,'promStart'] <- ref2[i,]$txEnd - 2000
  ref2[i,'promEnd'] <- ref2[i,]$txEnd + 2000
}

refGene <- rbind(ref1,ref2)
remove(ref1,ref2)

# process refGene dataset to set bins
chrs <- levels(factor(refGene$chr))
bins_ref <- data.frame(matrix(ncol=dim(refGene)[2],nrow=0))
colnames(bins_ref) <- colnames(refGene)
bin_pos1 = c(1)
for (chr in chrs){
  for (char in c('+','-')){
    bin <- refGene[which((refGene$chr == chr & refGene$strand == char)),]
    bins_ref <- rbind(bins_ref, bin)
    bin_pos1 <- append(bin_pos1, dim(bin)[1] + bin_pos1[length(bin_pos1)])
  }
}
remove(refGene)

# process CpG dataset to set bins
bins_CpG <- data.frame(matrix(ncol=dim(CpG)[2],nrow=0))
colnames(bins_CpG) <- colnames(CpG)
bin_pos2 = c(1)
for (chr in chrs){
  for (char in c('+','-')){
    bin <- CpG[which((CpG$chr == chr & CpG$strand == char)),]
    bins_CpG <- rbind(bins_CpG, bin)
    bin_pos2 <- append(bin_pos2, dim(bin)[1] + bin_pos2[length(bin_pos2)])
  }
}
remove(CpG)


# calculate the methylation levels
for (i in 1:(length(bin_pos1)-1)){
  gene_bin <- bins_ref[bin_pos1[i]:bin_pos1[i+1]-1, ]
  CpG_bin <- bins_CpG[bin_pos2[i]:bin_pos2[i+1]-1, ]
  for (j in 1:dim(gene_bin)[1]){
    select <- CpG_bin[which(CpG_bin$base >= gene_bin[j,'promStart'] & CpG_bin$base <= gene_bin[j,'promEnd']),]
    bins_ref[bin_pos1[i]+j-1, 'methylation'] <- apply(select['freqC'],2,mean)
  }
}

# sort bins_ref by methylation levels
head(bins_ref[order(bins_ref$methylation,na.last = TRUE, decreasing = TRUE),],10)
 
