# Part I
# 9.1
import re

# Get the seq info
file = open('data4/uniprot.fa','r')
output = open('data4/9.1','w')
id = ''
seq = ''
flag = False

regex = re.compile('C.{1,4}C')

for line in file:
    if line.startswith(">"):
        flag = True
        if seq != '':
            output.write('AC: %s\nSequences: %s\n' %(id,seq))
            dsulf = regex.findall(seq)
            if dsulf != []:
                output.write('Disulfide bond pattern: %s\n\n' % str(dsulf))
            else:
                output.write('Disulfide bond pattern: %s\n\n' % 'None')
        seq = ''
        id = line.split("|")[1]
        continue
    if flag:
        line = line.strip()
        seq = seq + line

output.write('AC: %s\nSequences: %s\n')
dsulf = regex.findall(seq)
if dsulf != []:
    output.write('Disulfide bond pattern: %s\n\n' % dsulf)
else:
    output.write('Disulfide bond pattern: %s\n\n' % 'None')

file.close()
output.close()

Part of output file：
 

# 9.2

import re
from string import punctuation
# Find 'whale' and 'captain'
wrd1 = re.compile(r'whale\b', re.IGNORECASE)
wrd2 = re.compile(r'captain\b', re.IGNORECASE)
l1 = 0
l2 = 0
text = ''    # text content

for line in open('data4/White Whale.txt','r'):
    l1 += len(wrd1.findall(line))
    l2 += len(wrd2.findall(line))
    line = line.lower().strip()
    text = text + re.sub('[%s]' % punctuation, ' ', line)

print('The count of whale: %d' %l1)
print('The count of captain: %d' %l2)

words = set(text.split())

output = open('data4/9.2', 'w')

for word in words:
    if len(word) > 1 and word != 'a':    # Exculde the single character
        count = text.count(word)
        if count > l1:
            output.write('%s: %d (> count of \'whale\')\n' %(word, count))
        elif count > l2:
            output.write('%s: %d (> count of \'captain\')\n' %(word, count))
        else:
            continue

output.close()

Part of output file：
 

# 9.3
# Sequences form uniprot.fasta
import re
flag = False
info = ['','']
jd = False
flt = re.compile('kinase.*OS=.*OX')
p = re.compile('R.[ST][^P]')

output = open('data4/9.3','w')

for line in open('data4/uniprot.fa','r'):
    line = line.strip()
    if line.startswith('>'):
        if info[1] != '' and jd != False:

            output.write('AC: %s\nSequence: %s\nPhosphorylation: ' %(info[0],info[1]))
            pho = p.findall(info[1])
            output.write(str(pho))
            output.write('\n\n')
            print('Write one record!')

        info = ['','']
        jd = False
        flag = True
        info[0] = line.split('|')[1]

        x = flt.search(line.split('|')[2])
        if x != None:
            jd = True
        continue

    if flag and jd:
        info[1] = info[1] + line

if info[1] != '' and jd != False:
    output.write('%s\n%s\nPhosphorylation: ' %(info[0],info[1]))
    pho = p.findall(info[1])
    output.write(pho)
    output.write('\n')
    print('Write one record!')

output.close()

Part of output file：
 

# 9.4
import re,requests
url = 'https://pubmed.ncbi.nlm.nih.gov/33053381/'
user_agents = {'User-agent': 'Mozilla/8.0'}
html = requests.get(url, headers=user_agents)
html.encoding = 'utf-8'
if html.status_code == 200:
    print("Successfully Request!")
else:
    print('Fail to request url.')

text = html.text
reg_author = re.compile('<meta name=\"citation_authors\" content=\"(.*)\">')
author = reg_author.search(text).group(1)
authors = author.split(';')
for author in authors:
    print(author)

 

# 9.5
import re,requests
import bs4
url = 'https://pubmed.ncbi.nlm.nih.gov/33053381/'
user_agents = {'User-agent': 'Mozilla/8.0'}
html = requests.get(url, headers=user_agents)
html.encoding = 'utf-8'
if html.status_code == 200:
    print("Successfully Request!")
else:
    print('Fail to request url.')

soup = bs4.BeautifulSoup(html.text, 'lxml')
author_info_text = soup.find_all('div', class_="authors-list")[0]
author_info_text = str(author_info_text)

filter = re.compile('linksrc=author_name_link">(.*)</a>')
authors = filter.findall(author_info_text)
for author in authors:
    print(author)

 
# 10.1
def fastaCount(fasta_file):
    count = 0
    for line in fasta_file:
        if line.startswith('>'):
            count += 1
    return count

if __name__ == '__main__':
    fasta = open('data4/SwissProt.fa','r')
    count = fastaCount(fasta)
    print(count)
    fasta.close()

 

# 10.2
def parser(fasta_file):
    flag = False
    info = ['','']
    for line in fasta_file:
        line = line.strip()
        if line.startswith(">"):
            if info[1] != '':
                fastaNew(info)
                info[1] = ''
                info[0] = ''
            flag = True
            info[0] = line.split('|')[1]
            continue
        if flag:
            info[1] = info[1] + line

    fastaNew(info)

def fastaNew(info):
    newfile = open('data4/10.2_' + info[0],'w')
    newfile.write('>' + info[0] + '\n')
    newfile.write(info[1] + '\n')
    newfile.close()
    print('Sucessfully write ' + info[0] + '!')


if __name__ == '__main__':
    file = open('data4/SwissProt.fa','r')
    parser(file)
    file.close()

# 10.3
import math,struct

def distance(x, y, z):
    dis = math.sqrt(pow(x, 2) + pow(y, 2) + pow(z, 2))
    return dis

def getInfo(pdb_file):
    pdb_format = '6s5s1s4s1s3s1s1s4s1s3s8s8s8s6s6s10s2s3s'
    atoms = {}
    CA_count = 0
    for line in pdb_file:
        if line[0:4] == 'ATOM':
            tmp = struct.unpack(pdb_format, line.encode('utf-8'))
            atom_type = tmp[3].decode('utf-8').strip()
            chain = tmp[7].decode('utf-8')
            res_num = tmp[8].decode('utf-8').strip()
            x = float(tmp[11].strip())
            y = float(tmp[12].strip())
            z = float(tmp[13].strip())

            if atom_type == 'CA':
                CA_count += 1
                if chain not in atoms.keys():
                    atoms[chain] = [[res_num, x, y, z]]
                else:
                    atoms[chain].append([res_num, x, y, z])
    return atoms


if __name__ == '__main__':
    pdb = open('data4/1TLD.pdb', 'r')
    atoms = getInfo(pdb)
    min_dis = 1000
    min_ord = []
    for key in atoms.keys():
        arr = atoms[key]
        l = len(arr)
        for i in range(l - 1):
            for j in range(i + 1, l):
                dis = distance(arr[i][1] - arr[j][1], arr[i][2] - arr[j][2], arr[i][3] - arr[j][3])
                if dis < min_dis:
                    min_dis = dis
                    min_ord = [arr[i][0], arr[j][0]]
        print('The minimum distance between resdue-%s and resdue-%s is %.3f.'%(min_ord[0], min_ord[1], min_dis))
 

# 10.4
# Checked
import math, struct

def distance(x, y, z):
    dis = math.sqrt(pow(x, 2) + pow(y, 2) + pow(z, 2))
    return dis

# dic: {[key- chain ] : [value- [res_num, x, y, z] ]}
def getInfo(pdb_file):
    pdb_format = '6s5s1s4s1s3s1s1s4s1s3s8s8s8s6s6s10s2s3s'
    atoms = {}
    CA_count = 0
    for line in pdb_file:
        if line[0:4] == 'ATOM':
            tmp = struct.unpack(pdb_format, line.encode('utf-8'))
            atom_type = tmp[3].decode('utf-8').strip()
            chain = tmp[7].decode('utf-8')
            res_num = tmp[8].decode('utf-8').strip()
            x = float(tmp[11].strip())
            y = float(tmp[12].strip())
            z = float(tmp[13].strip())

            if atom_type == 'CA':
                CA_count += 1
                if chain not in atoms.keys():
                    atoms[chain] = [[res_num, x, y, z]]
                else:
                    atoms[chain].append([res_num, x, y, z])

    return atoms

if __name__ == '__main__':
    pdb = open('data4/3G5U.pdb','r')
    atoms = getInfo(pdb)
    keys = list(atoms.keys())
    output = open('data4/10.4', 'w')

    for i in range(len(atoms[keys[0]])):
        for j in range(len(atoms[keys[1]])):
            a1 = atoms[keys[0]][i]
            a2 = atoms[keys[1]][j]
            dis = distance(a1[1] - a2[1], a1[1] - a2[1], a1[1] - a2[1])
            if dis < 6.0:
                output.write('One atom between A chain and B chain: %.3f.\n' %dis)

    output.close()


# 10.5
sequence = raw_input("Type the sequence filename: ")
predictor = raw_input("1 (disorder), 2 (sse), or 3
   (accessibility): ")
F = open(sequence)
if predictor == '1': prediction = disorder(F)
elif predictor == '2': prediction = sse(F)
else: prediction = accessibility(F)

# fasta file analysis
def fasta_parser(fasta_file):
    # info format: [[index, seq]]
    info = []
    seq = ''
    index = ''
    flag = False
    for line in fasta_file:
        line = line.strip()
        if line.startswith('>'):
            if seq != '':
                info.append([index, seq])
            seq = ''
            index = line.split('|')[1]
            flag = True
            continue
        if flag:
            seq = seq + line
    info.append([index, seq])

    return info

# codon frame analysis
def codon(DNA_seq_info):
    seq = DNA_seq_info

    for frame in range(3):
        start = 0
        stop = 0
        i = frame
        while i < len(seq):
            codon = seq[i: i +3]
            if codon == 'AUG':
                start = start + 1
            if codon == 'UAG' or codon == 'UAA' or codon == 'UGA':
                stop = stop + 1
            i = i + 3
        print("Frame %d:" %(frame + 1))
        print("Start codon: %d" % start)
        print("Stop codon: %d" % stop)

# secondary structure analysis
def secondary_structure(protein_seq_info):
    residues = protein_seq_info

    pref = {'A': [1.45, 0.97],
            'C': [0.77, 1.3],
            'D': [0.98, 0.80],
            'E': [1.53, 0.26],
            'F': [1.12, 1.28],
            'G': [0.53, 0.81],
            'H': [1.24, 0.71],
            'I': [1.00, 1.60],
            'K': [1.07, 0.74],
            'L': [1.34, 1.22],
            'M': [1.20, 1.67],
            'N': [0.73, 0.65],
            'P': [0.59, 0.62],
            'Q': [1.17, 1.23],
            'R': [0.79, 0.90],
            'S': [0.79, 0.72],
            'T': [0.82, 1.20],
            'V': [1.14, 1.65],
            'W': [1.14, 1.19],
            'Y': [0.61, 1.29]}

    strc = ''
    for i in residues:
        if pref[i][0] >= 1 and pref[i][1] < pref[i][0]:
            strc += 'H'
        elif pref[i][1] >= 1 and pref[i][1] > pref[i][0]:
            strc += 'E'
        else:
            strc += 'L'

    # Search for secondary structure

    # Output results
    print("Input:")
    print(residues)
    print('Output:')
    print(strc)

# Solution accessibility analysis
def accessibility(protein_seq_info):
    expose_value = {'A': 0.48,
                    'C': 0.32,
                    'D': 0.81,
                    'E': 0.93,
                    'F': 0.42,
                    'G': 0.51,
                    'H': 0.66,
                    'I': 0.39,
                    'K': 0.93,
                    'L': 0.41,
                    'M': 0.44,
                    'N': 0.82,
                    'P': 0.78,
                    'Q': 0.81,
                    'R': 0.84,
                    'S': 0.70,
                    'T': 0.71,
                    'V': 0.40,
                    'W': 0.49,
                    'Y': 0.67}
    threshold = 0.7

    # Set up residues sequences
    residues = protein_seq_info

    solu = ''
    for re in residues:
        if expose_value[re] > threshold:
            solu = solu + re.upper()
        else:
            solu = solu + re.lower()

    print('Input:', residues)
    print('Output:', solu)

# call an analysis function
def call_fun(file_type, func_type, seq_info):
    if file_type == 'DNA' and func_type == 1:
        codon(seq_info)
    elif fileType == 'Protein' and func_type == 2:
        secondary_structure(seq_info)
    elif fileType == 'Protein' and func_type == 3:
        accessibility(seq_info)
    else:
        print('Function calling failed.')

# main function: Get input and then analysis the file
if __name__ == '__main__':
    # User Input
    # seq file type
    fileType_list = ['DNA', 'Protein']
    fileType_num = int(input('''Please input the type of file you want to analyze:\n(1) -- DNA, (2) -- Protein\nYou must choose an index number\n'''))
    while fileType_num not in [1, 2]:
        print('File type choice failed. \n\nTry again:')
        fileType_num = int(input('''Please input the type of file you want to analyze:\n((1) -- DNA, (2) -- Protein\nYou must choose an index number\n'''))
    fileType = fileType_list[fileType_num - 1]
    print("Successfully choose %s file!\n" % fileType)

    # seq file path
    fullPath = input('''Please input your fasta file\'s absolute path: (Info in this file must be only-one sequence)\n''')

    # choose analysis function
    func = int(input('''Please input the function you want to call to analyze file:\n(1) -- codon analysis of DNA seq\n(2) -- secondary structure analysis of protein seq\n(3) -- solution accessiblity analysis of protein seq\nYou must choose an index number correspond to your seq tyoe.\n'''))

    file = open(fullPath,'r')

    info = fasta_parser(file)

    for i in range(len(info)):
        seq = info[i][1]
        print('\n' + info[i][0])
        if seq != '':
            call_fun(fileType, func, seq)

 

# Part II
# palindrome sequences analysis
# Checked
# Get index and seq information from fasta file
def fastaParser(fasta_file):
    # info format: [[index, seq]]
    info = []
    seq = ''
    chr = ''
    flag = False
    for line in fasta_file:
        line = line.strip()
        if line.startswith('>'):
            if seq != '':
                info.append([chr, seq])
            seq = ''
            chr = line.replace('>','')
            flag = True
            continue
        if flag:
            seq = seq + line
    info.append([chr, seq])

    return info

# Analyze palindrome sequences with different length in a read of seq
def paliAnalyzer(seq, length_min, length_max):
    # pali_list format = [palibox_len(int), paliseq(list), pali_count(int)]
    pali_list = []
    l = len(seq)
    for n in range(length_min, length_max + 1):  # range args set: range(arg1, arg2) = [arg1 ~ arg2 - 1]
        # pali_arr format: [palindrome sequence, start, end]
        pali_arr = []
        pali_count = 0

        for i in range(l - n):
            box = seq[i:i+n]
            ifpali = reverse_pair_box(box)
            if box == ifpali:
                pali_arr.append([box, i, i+n])
                pali_count += 1
        pali_list.append([n, pali_arr, pali_count])

    print('Done a seq!')

    return pali_list

# Get the corresponding palindrome seq of an exact seq
def reverse_pair_box(box):
    pair_dic = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    box = list(box)
    box.reverse()
    rev_paired = ''

    for i in range(len(box)):
        rev_paired += pair_dic[box[i]]

    return rev_paired


# Main function
if __name__ == '__main__':
    fasta = open('data4/sacCer2.fa','r')
    output = open('data4/N2','w')

    info = fastaParser(fasta)
    fasta.close()

    brief = open('data4/N2_brief','w')

    for i in range(len(info)):
        lists = paliAnalyzer(info[i][1], 4, 12)
        if lists != []:
            for n in range(len(lists)):
                output.write('%s: %d bp\nPalidrome seq: %s\nPalidrome count: %d\n\n' % (str(info[i][0]), lists[n][0], str(lists[n][1]), lists[n][2]))
                brief.write('%s: %d bp | Palidrome count: %d\n' %(str(info[i][0]), lists[n][0], lists[n][2]))
                print('%s: %d bp | Palidrome count: %d' %(str(info[i][0]), lists[n][0], lists[n][2]))
        brief.write('\n')
        print('Done %s !' % info[i][0])

    output.close()
    brief.close()

