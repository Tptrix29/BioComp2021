# hw3_2.sh

#! /bin/bash
rm -rf 2_re
dir=($(seq 1 22) "X" "Y")
for i in ${dir[@]}
do
# + strand
chr="chr"$i"\b.*+"
length=`grep $chr pdata.bed | wc -l`
length=`expr $length - 1`
left=(`grep $chr pdata.bed | awk '{print $2}'` )
right=(`grep $chr pdata.bed | awk '{print $3}'` )

for num in `seq 0 $length`
do
d=${left[$num]}
u=`expr ${right[$num]} - 1`
grep $chr promoter.gtf | awk '{
    if (("'$d'" + 3000) <= $2){
        if (("'$u'" + 3000) >= $2)
        {print $0}
    }
    else {
        if (("'$d'" - 3000) <= $2)
        {print $0}
    }
}' >> 2_re
echo $chr
done
echo $i"+ DONE!"

# - strand
chr="chr"$i"\b.*-"
length=`grep $chr pdata.bed | wc -l`
length=`expr $length - 1`
left=(`grep $chr pdata.bed | awk '{print $2}'` )
right=(`grep $chr pdata.bed | awk '{print $3}'` )

for num in `seq 0 $length`
do
d=${left[$num]}
u=`expr ${right[$num]} - 1`
grep $chr promoter.gtf | awk '{
    if (("'$d'" + 3000) <= $3){
        if (("'$u'" + 3000) >= $3)
        {print $0}
    }
    else {
        if (("'$d'" - 3000) <= $3)
        {print $0}
    }
}' >> 2_re
done
echo $i"- DONE!"

done

# Results output command
### 2
# wc -l 2_re
### 3
# sort 2_re | uniq | wc -l
### 4
# sort 2_re | uniq -c | sort -nr | head -n 5

