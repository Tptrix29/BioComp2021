# hw3_1.sh


#! /bin/bash
rm -rf 1_re
dir=($(seq 1 22) "X" "Y")
for i in ${dir[@]}
do
# + strand
chr="chr"$i"\b.*+"
st=(`grep $chr promoter.gtf | awk '{print $2}'` )

for s in ${st[@]}
do
d=`expr $s - 3000`
u=`expr $s + 3000`
grep $chr pdata.bed | awk '{
    if ($2 <= "'$d'"){
        if ($3 >= "'$d'")
        {print $0}
    }
    else {
        if ($2 <= "'$u'")
        {print $0}
    }

}' >> 1_re
done
echo $chr
echo $i"+ DONE!"

# - strand
chr="chr"$i"\b.*-"
st=(`grep $chr promoter.gtf | awk '{print $3}'` )

for s in ${st[@]}
do
d=`expr $s - 3000`
u=`expr $s + 3000`
grep $chr pdata.bed | awk '{
    if ($2 <= "'$d'"){
        if ($3 >= "'$d'")
        {print $0}
    }
    else {
        if ($2 <= "'$u'")
        {print $0}
    }
}' >> 1_re
done
echo $i"- DONE!"

done

# Result output command
# wc -l 1_re

