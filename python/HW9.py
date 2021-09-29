# Part I
# 14.1
# first.py:
def write_num(file_name):
    num = input("Please input the number you want to write: ")
    file = open(file_name, 'w')
    file.write(num)
    print("Number writing done!")
    file.close()
    return None


if __name__ == '__main__':
    write_num('results/14.1')

# second.py:
def read_num(file_name):
    line = None
    for line in open(file_name):
        line = line.strip()
    num = float(line)
    return num


def cal_square(num):
    square = num * num
    return square


if __name__ == '__main__':
    num = read_num('results/14.1')
    square = cal_square(num)
    print('The number is %.1f' % num)
    print("The square of the number is %.1f" % square)

 
# 14.2
import os


def cat_run(py1, py2):
    try:
        os.system("python3.8 " + py1)
    except:
        print("First False.")
        raise SystemExit
    else:
        try:
            os.system("python3.8 " + py2)
        except:
            print("Second False.")
            raise SystemExit
        else:
            print("Done!")

    return None


if __name__ == '__main__':
    file1 = 'first.py'
    file2 = 'second.py'
    cat_run(file1, file2)

 

# 14.3
import os, sys


def cat_run(py1, py2):
    try:
        os.system("python3.8 " + py1)
    except:
        print("First False.")
        raise SystemExit
    else:
        try:
            os.system("python3.8 " + py2)
        except:
            print("Second False.")
            raise SystemExit
        else:
            print("Done!")

    return None


def get_file():
    py1 = sys.argv[1]
    py2 = sys.argv[2]
    return py1, py2


if __name__ == '__main__':
    file1, file2 = get_file()
    cat_run(file1, file2)

 
# 14.4
import os


def file_num(path):
    os.chdir(path)
    num = len(os.listdir())
    print('The file number of your path is %d.' % num)


if __name__ == '__main__':
    path = '/Users/tianpei'
print('Your path:', path)
    file_num(path)

 
# 14.5
from Bio.Blast import NCBIWWW, NCBIXML


def blast2xml(query, query_type):
    if query_type == 'nucl':
        para = 'blastn'
    elif query_type == 'prot':
        para = 'blastp'
    else:
        print('Query type is error.')
        raise SystemExit
    xml_file = 'results/' + query + '_' + para + '.xml'
    BlastResult_handle = NCBIWWW.qblast(para, 'nr', query, format_type='XML')
    BlastOut = open(xml_file, 'w')
    BlastOut.write(BlastResult_handle.read())
    BlastOut.close()
    BlastResult_handle.close()
    print('Blast Done!')
    return xml_file

def xml2fasta(xml_file):
    file = open(xml_file, 'r')
    blast_out = NCBIXML.parse(file)
    fasta = open(xml_file.split('.')[0] + '.fasta', 'w')

    for record in blast_out:
        for alignment in record.alignments:
            fasta.write('>' + alignment.title + '\n')
            for hsp in alignment.hsps:
                if hsp.expect < 0.0001:
                    fasta.write(hsp.match + '\n\n')

    print('Parse Done!')


if __name__ == '__main__':
    xml = blast2xml('P05480', 'prot')
    xml2fasta(xml)

 
# Introduction
# 练习15.1 数据类型
# 在aaRS项目的骨架程序中，会为变量seq、directory、filename和sequences采用什么数据类型？
# seq-字符串，directory-字符串，filename-字符串，sequences-列表

# 练习15.2 跨膜螺旋预测（Bacteriorhodopsin.fasta，lysozyme.fasta）
# 写下如下项目描述的需求：有一个包含跨膜螺旋氨基酸相对频率的表格。一般来说，非极性氨基酸出现的频率高于极性氨基酸。基于数据为跨膜螺旋氨基酸开发一个简单的预测器。程序应该从FASTA文件读取蛋白质序列并在序列上运行滑动窗口（见第2章）。通过表总结出每个长度为N的序列的频率。如果总数高于给定阈值，程序应该打印出跨膜螺旋发现的信息以及序列、位置。使用噬菌调理素（bacteriorhodopsin）和溶菌酶（lysozyme）的蛋白质序列测试程序。确定一个两种蛋白质都能清晰分辨的阈值参数。

# 练习15.3 创建基架
# 执行跨膜螺旋预测器的项目基架。写下在编写完整代码前会询问的关于项目的三个最重要的问题。

# 项目目的？函数定义？输入与输出？

# 练习15.4 执行程序
# 实现跨膜螺旋预测器。
"""
py6_15.py
Predict the helix structure of amino acid sequence.
"""


def read_table(seq_table):
    """
    无参考表格，无法完善
    :param seq_table: reference table
    :return: list of table
    """
    return None


def read_fasta(fasta_file):
    """
    Analyze the fasta file and get the seq info
    :param fasta_file: sequence file path
    :return: seq_info list
    """
    pro_seq_list = []    # list of seq info
    flag = False
    pro_seq = ''
    for line in open(fasta_file):
        line = line.strip()
        if line.startswith('>'):
            if pro_seq != '':
                pro_seq_list.append(pro_seq)
            pro_seq = ''
            flag = True
            continue
        if flag:
            pro_seq += line

    pro_seq_list.append(pro_seq)

    return pro_seq_list


def cal_mer(pro_seq, k):
    """
    Analysis the seqs, and get the kmer info
    :param pro_seq: seq_info list
    :param k: length of box--k amino acid
    :return: kmer info dictionary, with the value of start point and end point of each mer
    """
    mer_info = {}
    for i in range(len(pro_seq) - k + 1):
        mer = pro_seq[i:i + k]
        if mer in mer_info.keys():
            mer_info[mer][0] += 1
            mer_info[mer][1].append([i + 1, i + k])
        else:
            mer_info[mer] = [1, [i + 1, i + k]]
    return mer_info


def threshold(kmer_info):
    """
    无预测参考，无法进行分析
    :param kmer_info: output of cal_kmer
    :return: analysis result
    """
    pass


if __name__ == '__main__':
    seq1 = read_fasta('data/Bacteriorhodopsin.fasta')
    seq2 = read_fasta('data/lysozyme.fasta')
    print(seq1, seq2)
    info1 = cal_mer(seq1[0], 8)
    print(info1)
    info2 = cal_mer(seq2[0], 8)
    print(info2)
    print(len(info1), len(seq1[0]))


# 练习15.5 运行pylint
# 在其中一个程序上运行pylint。完善格式，使得分至少为9.0分。
 

# Part II
import random


def get_seqs(file):
    seq_list = []
    flag = False
    seq = ''
    for line in open(file, 'r'):
        line = line.strip()
        if line.startswith('>'):
            if seq != '':
                seq_list.append(seq)
            flag = True
            seq = ''
            continue
        if flag:
            seq += line
    seq_list.append(seq)
    return seq_list


def shotgun(seqs_list):
    rest_list = seqs_list
    matched_seq = random.choice(seqs_list)
    rest_list.remove(matched_seq)
    while rest_list:
        most_match, matched_seq = match_most_one(matched_seq, rest_list)
        if most_match in rest_list:
            rest_list.remove(most_match)
    return matched_seq


def match_most_one(matched_seq, rest_list):
    most_match = [0, '', '', False]
    l = len(rest_list[0])
    for k in range(l):
        lth = l - k
        left_ma = matched_seq[:lth]
        for rs in rest_list:
            if rs[k:] == left_ma:
                most_match = [lth, rs, rs[k:], False]
                break
        right_ma = matched_seq[k:]
        for rs in rest_list:
            if rs[:lth] == right_ma and lth > most_match[0]:
                most_match = [lth, rs, rs[:lth], True]
                break
        if most_match[0] > 0:
            break

    if most_match[3]:
        matched_seq = matched_seq + most_match[1].replace(most_match[2], '', 1)
    else:
        matched_seq = most_match[1] + matched_seq.replace(most_match[2], '', 1)
    return most_match[1], matched_seq


def iteration_assembly(path, iter):
    """
    heuristic assembly
    """
    min_len = 100000
    best_match = ''
    for i in range(iter):
        seq_list = get_seqs(path)
        match = shotgun(seq_list)
        if len(match) < min_len:
            min_len = len(match)
            best_match = match
    return best_match


if __name__ == '__main__':
    best = iteration_assembly('data/sequence_assembly.fasta', 5)
    print(best)
    print(len(best))

 





