
#1 前1000000列数据按染色体顺序储存为new1.bed/前1000000列数据按起始位点储存为new2.bed
sed -n '1,1000000p' CTCF.bed | sort > new1.bed
sed -n '1,1000000p' CTCF.bed | sort -n -k2 > new2.bed


#2 降序排列每条染色体数据数
cut -f 1 new2.bed | sort | uniq -c | sort -nr


#3 chr10上至少出现1次和只出现1次的数据数
#only 1
grep "chr10" new2.bed | cut -f 1-3,6 | uniq -c | grep "1.*c" | wc -l
#at least 1
grep "chr10" new2.bed | cut -f 1-3,6 | uniq -c | wc -l


#4 除了chrM外出现最多的数据
grep -v "chrM" new2.bed | cut -f 1-3,6 | uniq -c | sort | tail -n 1


#5 常染色体上出现5次及以上的数据数
grep "chr[1-9]" new2.bed | cut -f 1-3,6 | uniq -c | grep -v "[1-4]\D.*c" | wc -l

