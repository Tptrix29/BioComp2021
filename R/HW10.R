# Required Packages: DBI, RMySQL
if (!requireNamespace("RMySQL", quietly = TRUE))
	install.packages("RMySQL")
if (!requireNamespace("DBI", quietly = TRUE))
	install.packages("DBI") 


# 1.1
library(DBI)
library(RMySQL)
con = dbConnect(MySQL(),user="genomep",password="password",dbname="mm9",
host="genome-mysql.cse.ucsc.edu")
dbListTables(con)
sql<-"SELECT * from refGene"
refGene<-dbGetQuery(con,sql)
dbDisconnect(con)

target <- refGene[which(refGene$chrom == 'chr12' & refGene$txStart >= 20000000 & refGene$txStart <= 28000000),]


# 1.2
data.frame(name = refGene$name, length = refGene$txEnd - refGene$txStart)


# 2.1
setwd("/Users/tianpei/BioComp_Homework/R_Homework/R1")
t <- read.table("data/ChildrenHigh.tab", header = TRUE, stringAsFactors = FLASE)
first <- t[which(t$childNum==001),]
mean(first$childHeight)
# [1] 69.82098


# 2.2
boys <- t[which(t$gender=='male'), ]
girls <- t[which(t$gender=='female'), ]
mean(boys$childHeight)
# [1] 69.2341
mean(girls$childHeight)
# [1] 64.10397
sd(boys$childHeight)
# [1] 2.623905
sd(girls$childHeight)
# [1] 2.355653


# 2.3
t['childHigh_cm'] <- t['childHeight'] * 2.54

 
# 2.4
dim(t)[1] / dim(first)[1]
# [1] 4.556098


# 3.1
setwd("/Users/tianpei/BioComp_Homework/R_Homework/R1")
seq <- read.table('data/scExpmat.txt',header = TRUE)
seq[,2:202] <- as.data.frame(lapply(seq[,2:202],as.numeric))
seq['rowSum'] <- rowSums(seq[,2:202])
selected_seq <- seq[which(seq$rowSum!=0),]
c(dim(seq)[1],dim(selected_seq)[1])
# [1] 20148 10865


# 3.2
setwd("/Users/tianpei/BioComp_Homework/R_Homework/R1")
seq <- read.table('data/scExpmat.txt',header = TRUE)
seq[,2:202] <- as.data.frame(lapply(seq[,2:202],as.numeric))
data <- seq[,2:202]
seq[,2:202] <- data[,order(colSums(data))]
 

