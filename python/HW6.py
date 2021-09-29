# Part I
# 6.1
file = open('HW_Python_3_data/SwissProt.fasta','r')
output = open('HW_Python_3_data/6-1_output.txt','w')
id = ''
flag = False
for line in file:
    if line.startswith(">"):
        flag = True
        id = line.split("|")[1]
        continue
    if flag:
        if line.startswith("M"):
            print(id)
            output.write(str(id) + "\n")
        flag = False

file.close()
output.close()


# 6.2
lineCounter = 1
odd = open('HW_Python_3_data/6-2_output_odd.txt','w')
even = open('HW_Python_3_data/6-2_output_even.txt','w')

for line in open('HW_Python_3_data/text.txt','r'):
    if lineCounter % 2 == 1:
        odd.write(line)
    else:
        even.write(line)
    lineCounter += 1
    
odd.close()
even.close()


# 6.3
file1 = open('HW_Python_3_data/test1.txt')
file2 = open('HW_Python_3_data/test2.txt')

data1 = []
data2 = []
for line1,line2 in zip(file1,file2):
    line1 = line1.strip()
    data1.append(line1)
    line2 = line2.strip()
    data2.append(line2)

file1.close()
file2.close()

inter = 0
only1 = 0
diff = 0
for i in range(len(data1)):
    if data1[i] in data2:
        inter += 1
    else:
        only1 += 1
        diff += 1
    if data2[i] not in data1:
        diff += 1

print("Intersection: %d\nOnly in text1: %d\nDifferences: %d" %(inter,only1,diff))


# 6.4
file1 = open('HW_Python_3_data/test1.txt')
file2 = open('HW_Python_3_data/test2.txt')

data1 = []
data2 = []
for line1,line2 in zip(file1,file2):
    line1 = line1.strip()
    data1.append(line1)
    line2 = line2.strip()
    data2.append(line2)

file1.close()
file2.close()

data1 = set(data1)
data2 = set(data2)
print(data1,data2)
print("Only in file1: > ",data1.difference(data2))
print("Only in file2: < ",data2.difference(data1))
print("Intersection of file1 and file2: # ",data1.intersection(data2))


# 6.5
file = open('HW_Python_3_data/transcripts.tracking','r')
filtered = open('HW_Python_3_data/6-5_output.txt','w')
for line in file:
    col = line.strip().split()
    exp = col[5:].count('-')
    print(len(col))
    if exp == 0:
        filtered.write(line)

file.close()
filtered.close()


# 7.1
file = open('HW_Python_3_data/lowry_data.txt','r')
table = []
for line in file:
    line = line.strip().split()
    table.append(line)

print(table)
add = ['0.17','0.091','0.096','0.099']
table.append(add)
print("After addition: \n")
print(table)


# 7.2
file = open('HW_Python_3_data/lowry_data.txt','r')
table = []
keys = []
header = True
for line in file:
    line = line.strip().split()
    if header:
        header = False
        for i in range(len(line)):
            table.append({line[i]:[]})
            keys = line
        continue
    else:
        for i,key in zip(range(len(line)),keys):
            table[i][key].append(line[i])

print(table)

file.close()


# 7.3
file = open('HW_Python_3_data/7-3.txt')
table = {}
bases = []
i = 0
for line in file:
    if i == 0:
        bases = line.strip().split()
        i += 1
    else:
        score = line.strip().split()
        table[score[0]] = {}
        for i in range(4):
            table[score[0]][bases[i]] = float(score[i+1])
        i += 1

file.close()
print(table)


# 7.4
seq1 = 'AGCAUCUA'
seq2 = 'ACCGUUCU'
similarity = 0
for base1,base2 in zip(seq1,seq2):
    score = table[base1][base2]
    similarity = similarity + score

print("Similarity score:  " + str(similarity))


# 7.5
# 7.5.1 Table in table
file = open('HW_Python_3_data/lowry_data.txt','r')
table = []
for line in file:
    line = line.strip().split()
    table.append(line)

print(table)
print("Second row:",table[1])
protein = []
for i in range(1,len(table)):
    protein.append(table[i][0])
print("Protein Concentration:",protein)

print('\n')

# 7.5.2 Dictionary in table
file = open('HW_Python_3_data/lowry_data.txt','r')
table = []
header = True
for line in file:
    line = line.strip().split()
    if header:
        header = False
        for i in range(len(line)):
            table.append({line[i]:[]})
            keys = line
        continue
    else:
        for i,key in zip(range(len(line)),keys):
            table[i][key].append(line[i])

print(table)
row2 = []
for i,key in zip(range(len(line)),keys):
    row2.append(table[i][key][0])
print("Second row:",row2)
print("Protein Concentration:",table[0]['protein'])

file.close()


# 8.1
from operator import itemgetter
file = open('HW_Python_3_data/lowry_data.txt','r')
table = []
for line in file:
    line = line.strip().split()
    table.append(line)
file.close()

print(table)

table = table[1:]
pro,ex1,ex2,ex3 = zip(*table)    # Transpose the table
ex = ex1 + ex2 + ex3
pro = pro * 3

new_table = [['protein','extinction']]
for cpro,nex in zip(pro,ex):
    new_table.append([cpro,nex])
print(new_table)
result = sorted(new_table[1:],key=itemgetter(1))
print(result)

output = open('HW_Python_3_data/8-1_output.txt','w')
for i in range(3):
    print(result[i])
    for j in range(len(result[i])):
        output.write(result[i][j] + '\t')
    output.write('\n')

output.close()


# 8.2
from operator import itemgetter
file = open('HW_Python_3_data/SwissProt.fasta','r')
info = []
seq = ''
title = ''
flag = False
for line in file:
    if line.startswith(">"):
        if seq != '':
            info.append([title,seq,len(seq)])
        flag = True
        title = line.strip()
        seq = ''
        continue
    if flag:
        seq = seq + line.strip()
info.append([title,seq,len(seq)])
print(info)
info = sorted(info,key=itemgetter(2),reverse=True)
print(info)

output = open('HW_Python_3_data/8-2_output.txt','w')
for i in range(len(info)):
    for j in range(len(info[i])):
        output.write(str(info[i][j]) + '\t')
    output.write('\n')

output.close()


# 8.3
# Read csv data and organize them in a dictionary
file = open('HW_Python_3_data/test.csv','r')
columns = {}
flag = True     # Need to initialize the dictionary element at first line
for line in file:
    read = line.strip().split(',')
    if flag == True:
        for i in range(len(read)):
            columns['column' + str(i+1)] = [read[i]]
        flag = False
    else:
        for i in range(len(read)):
            columns['column' + str(i+1)].append(read[i])
print(columns)

# sort each column by ascend from the last column to the first column
for i in range(len(columns)):
    index = 'column' + str(3-i)
    column = columns[index]
    print(index + ' sorted by ascend:',sorted(column))    # sort the column by ascend


# 8.4
file = open('HW_Python_3_data/SwissProt.fasta','r')
info = {}
seq = ''
ac = ''
flag = False
for line in file:
    if line.startswith(">"):
        if seq != '':
            info[ac] = seq
        flag = True
        ac = line.strip().split('|')[1]
        seq = ''
        continue
    if flag:
        seq = seq + line.strip()
info[ac] = seq
li = sorted(info.items(),key=lambda x:x[0])
print(info)
for i in li:
    index = i[0]
    print(index,info[index])


# 8.5
from operator import itemgetter
table = []
for line in open('HW_Python_3_data/BlastOut.csv','r'):
    info = line.strip().split(',')
    read = [float(info[-2]),info[1],line]    # Data structure transformation--str sorted by ASCII while float sorted by numeric value
    table.append(read)
    print(read)

print(table)
sorted_table = sorted(table,key=itemgetter(0))
print(sorted_table)
for i in range(len(sorted_table)):
    print(sorted_table[i][2])



# Part II
file = open("CTCF.bed",'r')

n = []
for i in range(1,23):
    n.append(i)
n.extend(['X','Y','M'])

# Create indexes according to chr & strand
nchr = []
for i in n:
    for j in ['+','-']:
        chr = 'chr'+str(i) + '_' + str(j)
        nchr.append(chr)
print(nchr)

# Analyze reads
bins = {}
count = {}
for line in file:
    line = line.strip()
    info = line.strip().split('\t')
    index,start,end = info[0] + '_' + info[5],int(info[1]),int(info[2])

    # confirm bin location
    st = int(start / 500)
    ed = int(end / 500) + 1
    k = ed - st

    for i in range(k):
        n = index + '_' + str((st + k) * 500) + '_' + str((st + k + 1) * 500)    # count for bins when one read was included in several bins
        if n in bins.keys():
            bins[n].append(line)
            count[n] += 1
            print("Append Success!")
        else:
            bins[n] = [line]
            count[n] = 1
            print("Creat Success!")    # if index isn't exist, creat the index with one read.

file.close()
print(count)
li = sorted(count.items(),key=lambda x:x[1],reverse=True)    # sort the bins by count
print(li)

output = open("HW_Python_3_data/CTCF_peak.bed",'w')

# Search for the bins with top 10000 reads number
i = 0
while i < 9999:
    index = li[i][0]
    print(count[index])
    output.write("# " + str(index) + '\n')
    output.write('# Count: ' + str(count[index]) + '\n')
    for read in bins[index]:
        output.write(read + '\n')
    output.write('\n')
    i += 1

output.close()

