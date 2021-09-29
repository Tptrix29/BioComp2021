# 1
# reads' centers in gene smad2
grep "chr18.*-" CTCF.bed | awk '
BEGIN {sum=0}
{cen=($2+$3-1)/2;
if (cen >= 45357922 && cen <= 45457515)
    sum++;
}
END {print sum}
'


# 2
# BED to GFF
cut -f 1-3,5-6 CTCF.bed | awk '
{a=substr($2,1,length($2)-4);
print $1, "\tchipseq", "\tinsulator\t", $2, "\t", $3-1, "\t",$4, "\t",$5, "\t.\t", $1 "_" a "0K_" a+1 "0K" 
}
' > CTCF.gff


# 3
# list top 5 bins
cut -f 9 CTCF.gff | sort | uniq -c | sort -r | head -n 5


# 4
# sub-bin groups and their data size
grep "chr17_37070K_37080K" CTCF.gff | awk '
{cen=($4+$5-1)/2;
est=substr(cen,7,8); #十位和个位提取，进行区间判定
sec=substr(cen,1,6); #区间百位及以上字段提取，便于生成区间
    if (est >50)
        print "chr17_" sec "50_" sec+1 "00";
    else
        print "chr17_" sec "00_" sec "50";
}
' | sort | uniq -c > buffer
# Output according to requirement
awk '{print $2 " - " $1}' buffer



