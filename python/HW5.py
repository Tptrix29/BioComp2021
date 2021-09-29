# Part I
# 3.1
cp = open("python_2_data/Results/3_1.txt",'w')
for line in open("python_2_data/第三章/neuron_data.txt",'r'):
    cp.write(line)
cp.close()


# 3.2
import numpy as np
data = []
for line in open("python_2_data/第三章/neuron_data.txt",'r'):
    data.append(float(line.strip()))
print(data)
mean = np.mean(data)
std = np.std(data)
print('The mean of the data is: ' + str(mean))
print('The std of the data is: ' + str(std))


# 3.3
A = 0
T = 0
C = 0
G = 0
count = 0
for line in open('python_2_data/第三章/genome.txt','r'):
    A = A + line.count('A')
    T = T + line.count('T')
    C = C + line.count('C')
    G = G + line.count('G')
    count = count + len(line) - 1   # Substrate the '\n'

A_fre = A / count
T_fre = T / count
C_fre = C / count
G_fre = G / count
max_fre = max(A_fre, T_fre, C_fre, G_fre)

print('The frequency of A is: %.2f' %A_fre)
print('The frequency of T is: %.2f' %T_fre)
print('The frequency of C is: %.2f' %C_fre)
print('The frequency of G is: %.2f' %G_fre)
print('The maximum frequency is: %.2f' %max_fre)


# 3.4
C = 0
G = 0
count = 0
for line in open('python_2_data/第三章/genome.txt','r'):
    C = C + line.count('C')
    G = G + line.count('G')
    count = count + len(line) - 1   # Substrate the '\n'

GC = (C + G) / count
print('The GC content is %.2f' %(GC * 100) + '%.')


# 3.5
A = 0
T = 0
C = 0
G = 0
count = 0
for line in open('python_2_data/第三章/genome.txt','r'):
    A = A + line.count('A')
    T = T + line.count('T')
    C = C + line.count('C')
    G = G + line.count('G')
    count = count + len(line) - 1   # Substrate the '\n'

A_fre = A / count
T_fre = T / count
C_fre = C / count
G_fre = G / count
max_fre = max(A_fre, T_fre, C_fre, G_fre)
GC = (C + G) / count

op = open('python_2_data/Results/3_5.txt','w')
op.write('The frequency of A is: %.2f \n' %A_fre)
op.write('The frequency of T is: %.2f \n' %T_fre)
op.write('The frequency of C is: %.2f \n' %C_fre)
op.write('The frequency of G is: %.2f \n' %G_fre)
op.write('The maximum frequency is: %.2f \n' %max_fre)
op.write('The GC content is %.2f' %(GC * 100) + '%. \n')

op.close()


# 4.1
count = 0
new = open('python_2_data/第四章/SwissProt.fasta','r')

for line in open('python_2_data/第四章/SwissProt.fasta','r'):
    if line[0] == '>':
        new.close()
        count = count + 1
        AC = line.split('|')[1].strip()
        new = open("python_2_data/Results/" + str(AC) + '.fasta','w')
    new.write(line)

new.close()


# 4.2
seq = ''
header = ''
op = open('python_2_data/Results/4_2.txt','w')
for line in open('python_2_data/第四章/SwissProt.fasta','r'):
    if line[0] == ">":
        if seq.startswith('M') and seq.count('W'):
            op.write(header)
            op.write(seq)
            op.write('\n')
        seq = ''
        header = line
        continue
    seq = seq + line

if seq.startswith('M') and seq.count('W'):
    op.write(header)
    op.write(seq)
    op.write('\n')

op.close()


# 4.3
A = 0
T = 0
C = 0
G = 0
count = 0
for line in open('python_2_data/第四章/AY810830.fasta'):
    if line[0] == '>':
        continue
    A = A + line.count('A')
    T = T + line.count('T')
    C = C + line.count('C')
    G = G + line.count('G')
    count = count + len(line) - 1  # Substrate the '\n'

A_fre = A / count
T_fre = T / count
C_fre = C / count
G_fre = G / count
AC = (C + A) / count
print('The frequency of A is: %.2f ' % A_fre)
print('The frequency of T is: %.2f ' % T_fre)
print('The frequency of C is: %.2f ' % C_fre)
print('The frequency of G is: %.2f ' % G_fre)
print('The GC content is %.2f' % (AC * 100) + '%.\n')


# 4.4
flag = False
for line in open('python_2_data/第四章/AY810830-1.fasta'):
    if line[0] == '>':
        if flag == True:
            A_fre = A / count
            T_fre = T / count
            C_fre = C / count
            G_fre = G / count
            AC = (C + A) / count
            print(header)
            print('The frequency of A is: %.2f ' % A_fre)
            print('The frequency of T is: %.2f ' % T_fre)
            print('The frequency of C is: %.2f ' % C_fre)
            print('The frequency of G is: %.2f ' % G_fre)
            print('The GC content is %.2f' % (AC * 100) + '%.\n')

        flag = True
        header = line[1:-1]
        A = 0
        T = 0
        C = 0
        G = 0
        count = 0
        continue
    A = A + line.count('A')
    T = T + line.count('T')
    C = C + line.count('C')
    G = G + line.count('G')
    count = count + len(line) - 1  # Substrate the '\n'

A_fre = A / count
T_fre = T / count
C_fre = C / count
G_fre = G / count
AC = (C + A) / count
print(header)
print('The frequency of A is: %.2f ' % A_fre)
print('The frequency of T is: %.2f ' % T_fre)
print('The frequency of C is: %.2f ' % C_fre)
print('The frequency of G is: %.2f ' % G_fre)
print('The GC content is %.2f' % (AC * 100) + '%.\n')


# 4.5
flag = False
seq = ''
for line in open('python_2_data/第四章/sequence.gb','r'):
    if line.startswith('ACCESSION'):
        if seq != '':
            print(header)
            seq = seq.upper()
            A = seq.count('A')
            T = seq.count('T')
            C = seq.count('C')
            G = seq.count('G')
            count = len(seq)

            A_fre = A / count
            T_fre = T / count
            C_fre = C / count
            G_fre = G / count

            print('The frequency of A is: %.2f ' % A_fre)
            print('The frequency of T is: %.2f ' % T_fre)
            print('The frequency of C is: %.2f ' % C_fre)
            print('The frequency of G is: %.2f \n' % G_fre)

            seq = ''
        header = line.split()[1]
    if line.startswith("ORIGIN"):
        flag = True
    if flag:
        if line.startswith('//'):
            flag = False
            continue
        field = line.split()
        seq = seq + ''.join(field[1:])

print(header)
seq = seq.upper()
A = seq.count('A')
T = seq.count('T')
C = seq.count('C')
G = seq.count('G')
count = len(seq)

A_fre = A / count
T_fre = T / count
C_fre = C / count
G_fre = G / count
print('The frequency of A is: %.2f ' % A_fre)
print('The frequency of T is: %.2f ' % T_fre)
print('The frequency of C is: %.2f ' % C_fre)
print('The frequency of G is: %.2f \n' % G_fre)


# 5.1
dic = {'UAA':'Stop',
       'UAG':'Stop',
       'UGA':'Stop',
       'AUG':'Start',
       'GGG':'Glycin'}


# 5.2
seq = ''
for line in open('python_2_data/第五章/A06662-RNA.fasta'):
       if line[0] == ">":
              header = line
              continue
       seq = seq + line[0:-1]

for frame in range(3):
       start = 0
       stop = 0
       i = frame
       while i < len(seq):
              codon = seq[i:i+3]
              if codon == 'AUG':
                     start = start + 1
              if codon == 'UAG' or codon == 'UAA' or codon == 'UGA':
                     stop = stop + 1
              i = i + 3
       print("Frame %d:" %(frame+1))
       print("Start codon: %d" %start)
       print("Stop codon: %d" %stop)
       print("\n")


# 5.3
import re
ab = ''
for line in open('python_2_data/第五章/Literature.txt','r'):
    ab = line

key = ['vaccine', 'COVID']
count = {}
sw = True

for i in key:
    count[i] = len(re.findall(i,ab))
    if count[i] == 0:
        sw = False
print("Abstract:\n",ab)
if sw == True:
    print("\nFound Keywords!")
print(count)


# 5.4
# Set up residues sequences
residues = ''
for line in open('python_2_data/第五章/P31946.fasta','r'):
       if line[0] == '>':
              header = line[0:-1]
              continue
       residues = residues + line[0:-1]

strc = ''
pref = {'A':[1.45,0.97],
        'C':[0.77,1.3],
        'D':[0.98,0.80],
        'E':[1.53,0.26],
        'F':[1.12,1.28],
        'G':[0.53,0.81],
        'H':[1.24,0.71],
        'I':[1.00,1.60],
        'K':[1.07,0.74],
        'L':[1.34,1.22],
        'M':[1.20,1.67],
        'N':[0.73,0.65],
        'P':[0.59,0.62],
        'Q':[1.17,1.23],
        'R':[0.79,0.90],
        'S':[0.79,0.72],
        'T':[0.82,1.20],
        'V':[1.14,1.65],
        'W':[1.14,1.19],
        'Y':[0.61,1.29]}

# Set up the dictionary for structure research
dic = {}
for i in pref:
       if pref[i][0] >=1 and pref[i][1] < pref[i][0]:
              dic[i] = 'H'
       elif pref[i][1] >= 1 and pref[i][1] > pref[i][0]:
              dic[i] = 'E'
       else:
              dic[i] = 'L'

# Search for secondary structure
for re in residues:
       strc = strc + dic[re]

# Output results
print(header)
print("Input:")
print(residues)
print('Output:')
print(strc)

 
# 5.5
expose_value = {'A':0.48,
                'C':0.32,
                'D':0.81,
                'E':0.93,
                'F':0.42,
                'G':0.51,
                'H':0.66,
                'I':0.39,
                'K':0.93,
                'L':0.41,
                'M':0.44,
                'N':0.82,
                'P':0.78,
                'Q':0.81,
                'R':0.84,
                'S':0.70,
                'T':0.71,
                'V':0.40,
                'W':0.49,
                'Y':0.67}
threshold = 0.7

# Set up residues sequences
residues = ''
for line in open('python_2_data/第五章/P31946.fasta','r'):
       if line[0] == '>':
              header = line[0:-1]
              continue
       residues = residues + line[0:-1]

solu = ''
for re in residues:
       if expose_value[re] > threshold:
              solu = solu + re.upper()
       else:
              solu = solu + re.lower()

print(header)
print('Input:',residues)
print('Output;',solu)



# Part II
# Initialize the count dictionary
count = {}
index = []
sum = 0
for i in range(22):
    index.append('chr'+str(i+1))
index = index + ['chrX','chrY','chrM']
print(index)

for i in index:
    count[i] = 0

# Calculate the reads number on each chromosome
for line in open('CTCF.bed','r'):
    field = line.split()
    if field[0] in count:
        count[field[0]] = count[field[0]] + 1

# Output the count dictionary
print(count)

# 运行结果：
# {'chr1': 279201, 'chr2': 252688, 'chr3': 197647, 'chr4': 173135, 'chr5': 175297, 'chr6': 180673, 'chr7': 166144, 'chr8': 146299, 'chr9': 126978, 'chr10': 148762, 'chr11': 152608, 'chr12': 151222, 'chr13': 88638, 'chr14': 100927, 'chr15': 97007, 'chr16': 103328, 'chr17': 121704, 'chr18': 68874, 'chr19': 97851, 'chr20': 70236, 'chr21': 39773, 'chr22': 50396, 'chrX': 88380, 'chrY': 20424, 'chrM': 10148}



