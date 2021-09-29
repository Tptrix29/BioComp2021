# Part I
# 11.1
class Channel:
    def __init__(self, num):
        names = ['Potassium channel', 'Mechanosensitivity channel', 'Chloride channel']
        pdbs = ['1jvm', '1msl', '1kpl']
        ang1s = [354.2, 359.2, 361.3]
        ang2s = [351.7, 345.7, 344.6]
        num -= 1
        self.name = names[num]
        self.pdb = pdbs[num]
        self.ang1 = ang1s[num]
        self.ang2 = ang2s[num]
        print('Initialization Done!')

    def show(self):
        print("Channel:\n%s, %s, %.1f, %.1f " % (self.name, self.pdb, self.ang1, self.ang2))


def usr_channel():
    try:
        print("Please input the index of channel you want to initialize:")
        num = input("(1)--Potassium channel, (2)--Mechanosensitivity channel, (3)--Chloride channel\n")
        num = int(num)
        ch = Channel(num)
    except IndexError:
        print('Error!')
        print('Please input the right index.')
    else:
        ch.show()


def list_channel():
    ch = []
    for i in range(3):
        index = i + 1
        ch.append(Channel(index))
    return ch


if __name__ == '__main__':
    chs = list_channel()
    print('\n')
    for ch in chs:
        ch.show()
        print('\n')


# 11.2
class Channel:
    def __init__(self, num):
        names = ['Potassium channel', 'Mechanosensitivity channel', 'Chloride channel']
        pdbs = ['1jvm', '1msl', '1kpl']
        ang1s = [354.2, 359.2, 361.3]
        ang2s = [351.7, 345.7, 344.6]
        num -= 1
        self.name = names[num]
        self.pdb = pdbs[num]
        self.ang1 = ang1s[num]
        self.ang2 = ang2s[num]
        print('Initialization Done!')


def list_channel():
    ch =[]
    for i in range(3):
        index = i + 1
        ch.append(Channel(index))
    return ch


if __name__ == '__main__':
    chs = list_channel()
    print('\n')
    for ch in chs:
        print('Name: %s' % ch.name)
        print('PDB: %s' % ch.pdb)
        print('Angle1: %.1f' % ch.ang1)
        print('Angle2: %.1f' % ch.ang2)
        print('\n')


# 11.3 + 11.4
class Channel:
    def __init__(self, num):
        names = ['Potassium channel', 'Mechanosensitivity channel', 'Chloride channel']
        pdbs = ['1jvm', '1msl', '1kpl']
        ang1s = [354.2, 359.2, 361.3]
        ang2s = [351.7, 345.7, 344.6]
        num -= 1
        self.name = names[num]
        self.pdb = pdbs[num]
        self.ang1 = ang1s[num]
        self.ang2 = ang2s[num]
        print('Initialization Done!')

    def show(self):
        print("Channel:\n%s, %s, %.1f, %.1f " % (self.name, self.pdb, self.ang1, self.ang2))


def list_channel():
    ch = []
    for i in range(3):
        index = i + 1
        ch.append(Channel(index))
    return ch


if __name__ == '__main__':
    chs = list_channel()
    for ch in chs:
        ch.show()


# 11.5
import numpy


class DendriticLengths:
    def __init__(self, file_name):
        self.len_list = []
        for l in open(file_name, 'r'):
            l = l.split()
            self.len_list.append(float(l[1]))
        print('Data set with %d dendritic lengths' % len(self.len_list))

    def get_average(self):
        avg = numpy.mean(self.len_list)
        print(avg)

    def get_sttddev(self):
        std = numpy.std(self.len_list)
        print(std)

    def __repr__(self):
        print('Data set with %d dendritic lengths' % len(self.len_list))


if __name__ == '__main__':
    n = 'data/neuron_lengths.txt'
    den = DendriticLengths(n)
    den.get_average()
    den.get_sttddev()


# 12.1
def evaluate_data(data, lower=100, upper=300):
    """Counts data points in three bins."""
    smaller = 0
    between = 0
    bigger = 0
    for length in data:
        if length < lower:
            smaller = smaller + 1
        elif lower < length < upper:
            between = between + 1
        elif length > upper:
            bigger += 1  #
    return smaller, between, bigger


def read_data(filename):
    "" "Reads neuron lengths from a text file."""
    primary, secondary = [], []  # NameError

    for line in open(filename):
        category, length = line.split()[0], line.split()[1]
        length = float(length)
        if category == "Primary":  # SyntaxError
            primary.append(length)
        elif category == "Secondary":
            secondary.append(length)
    return primary, secondary


def write_output_file(filename, count_pri, count_sec):
    """Writes counted values to a file."""
    output = open(filename, "w")
    output.write("Category  <100 100-300 >300\n")
    output.write("Primary : %5i %5i %5i\n" % count_pri)
    output.write("Secondary:%5i %5i %5i\n" % count_sec)
    output.close()


if __name__ == '__main__':
    try:
        primary, secondary = read_data('data/neuron_data.txt')  # IOErrors
    except:
        print('IOError')
    else:
        count_pri = evaluate_data(primary)
        count_sec = evaluate_data(secondary)
        write_output_file('data/results.txt', count_pri, count_sec)


# 12.2
def evaluate_data(data, lower=100, upper=300):
    """Counts data points in three bins."""
    smaller = 0
    between = 0
    bigger = 0
    for length in data:
        if length < lower:
            smaller = smaller + 1
        elif lower < length < upper:
            between = between + 1
        elif length > upper:
            bigger += 1  #
    return smaller, between, bigger


def read_data(filename):
    "" "Reads neuron lengths from a text file."""
    primary, secondary = [], []  # NameError

    for line in open(filename):
        category, length = line.split()[0], line.split()[1]
        length = float(length)
        if category == "Primary":  # SyntaxError
            primary.append(length)
        elif category == "Secondary":
            secondary.append(length)
    return primary, secondary


def write_output_file(filename, count_pri, count_sec):
    """Writes counted values to a file."""
    output = open(filename, "w")
    output.write("Category  <100 100-300 >300\n")
    output.write("Primary : %5i %5i %5i\n" % count_pri)
    output.write("Secondary:%5i %5i %5i\n" % count_sec)
    output.close()


if __name__ == '__main__':
    try:
        primary, secondary = read_data('data/neuron_data.txt')  # IOErrors
    except:
        print('IOError')
    else:
        count_pri = evaluate_data(primary)
        count_sec = evaluate_data(secondary)
        write_output_file('data/results.txt', count_pri, count_sec)


# 12.3
import numpy as np
l = []
for line in open('data/neuron_data_3.txt', 'r'):
    try:
        data = line.split()[1]
        data = float(data)
        l.append(data)
    except ValueError:
        print("ValueError.")
    else:
        continue

print(l)
mean = np.mean(l)
std = np.std(l)
print('The mean of data except the error line: %.2f' % mean)
print('The std of data except the error line: %.2f' % std)


# 12.4
import numpy as np

l = []
try:
    for line in open('data/neuron_data_3.txt', 'r'):
        try:
            data = line.split()[1]
            data = float(data)
            l.append(data)
        except ValueError:
            print("There is an invalid value in the file.")
        else:
            continue

    print(l)
    mean = np.mean(l)
    std = np.std(l)
    print('The mean of data except the error line: %.2f' % mean)
    print('The std of data except the error line: %.2f' % std)

except IOError:
    print('File open error.')


# 12.5
input_numbers = []
number = None
while number != 'q':
       number = raw_input("Insert a number: ")
       input_numbers.append(number)

def raw_input():
    input_num = []
    num = None
    while num != 'q':
        print('Please enter a number, it will be appended into the number array.')
        print('(Input \'q\' to quit and print the array.)')
        num = input('Your input:')
        if num == 'q':
            print('\n')
            continue
        try:
            num = float(num)
        except ValueError:
            print('Input Error! What you input is not a number!')
            print('Please input a number!\n')
            continue
        else:
            print('Valid input!\n')
            input_num.append(num)
            continue

    return input_num


if __name__ == '__main__':
    l = raw_input()
    print('The array you have input:')
    print(l)



# Part II
# analyze seqs in fasta file
def fasta_reader(file_path):
    seq = ''
    seq_list = []
    flag = False
    for line in open(file_path, 'r'):
        line = line.strip()
        if line.startswith('>'):
            if seq != '':
                seq_list.append(seq)
                seq = ''
            flag = True
            continue
        if flag:
            seq += line
    seq_list.append(seq)
    return seq_list


# find the base with max count on each position
def seq_align_count_max(seq_list):
    mseq = ''
    for i in range(len(seq_list[0])):
        dic = {'A': 0, 'T': 0, 'G': 0, 'C': 0}
        for j in range(len(seq_list)):
            index = seq_list[j][i]
            dic[index] += 1
        result = sorted(dic.items(), key=lambda item: item[1], reverse=True)
        n = 0
        add = result[n][0]
        while n < len(result) - 1:
            if result[n][1] == result[n + 1][1]:
                add += result[n + 1][0]
                n += 1
            else:
                break
        if len(add) > 1:
            add = '[' + add + ']'
        mseq += add

    return mseq


if __name__ == '__main__':
    path = 'data/seq.fa'
    seq_list = fasta_reader(path)
    print(seq_list)
    mseq = seq_align_count_max(seq_list)
    print('Seq Result: %s' % mseq)



# Part III
def fasta_parser(fasta_file_path):
    flag = False
    info_list = []
    name_info = []
    seq_info = []
    info = ['', '']
    for line in open(fasta_file_path, 'r'):
        line = line.strip()
        if line.startswith('>'):
            if info[1] != '':
                name_info.append(info[0])
                seq_info.append(info[1])
                print('Info of %s Done.' % info[0])
                info = ['', '']
            info[0] = line.split('|')[0].replace('>', '')
            info[1] = ''
            flag = True
            continue
        if flag:
            info[1] += line

    name_info.append(info[0])
    seq_info.append(info[1])
    return name_info, seq_info


# find each bin in the seq and output the read into file in format
def seq_bin(name_info_list, seq_info_list, bin_seq_list, bin_len):
    # open output file and set up a counter of each bin
    output = {}
    count = {}
    for seq in bin_seq_list:
        output[seq] = open('data/N3_%s' % seq, 'w')
        count[seq] = 0

    # analyze seq to find bin and its position, then out put read into output file
    for i in range(len(seq_info_list)):
        l = len(seq_info_list[i])
        for j in range(l - bin_len):
            end = j + bin_len
            box = seq_info_list[i][j:end]
            for seq in bin_seq_list:
                if box == seq:
                    output[seq].write('%s    %d    %d\n' % (name_info_list[i], j, end))
                    count[seq] += 1

    # add the count result to the end of output file and close it
    for seq in bin_seq_list:
        print('Total reads count of %s: %d' % (seq,count[seq]))
        output[seq].write('Total reads count: %d\n' % count[seq])
        output[seq].close()


if __name__ == '__main__':
    path = 'data/sacCer2.fa'
    names, seqs = fasta_parser(path)
    print(names)


    bins = ['AAGCTT', 'CCATGG', 'GTTAAC']
    seq_bin(names, seqs, bins, 6)







