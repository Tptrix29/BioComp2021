# Required Script: 
# hw3_dp.sh, hw3_1.sh, hw3_2.sh

# 1
bash hw3_dp.sh
bash hw3_1.sh
wc -l 1_re.txt
# 结果：311180


# 2
bash hw3_2.sh
wc -l 2_re.txt
# 结果：275417
   
   
# 3
sort 2_re.txt | uniq | wc -l
# 结果：18123
 

# 4
sort 2_re.txt | uniq -c | sort -nr | head -n 5
# 结果：200次 chr10 82617460 82752584 -

