# data processing
# BED file

grep -v "chrM" CTCF.bed | awk '{
if ($5 >= 10) print $0
}' | cut -f 1-3,6 | sort | uniq > pdata.bed

grep -v "chrM" gencode.v19.annotation.gtf | grep "\bgene\b" | cut -f 1,4,5,7 > promoter.gtf 

