# Part I
# 1.1
import math

# Parameter Initialization
G0 = -30.5
R = 0.00831
T = 298

# [ATP,ADP,Pi]
liver,muscle,brain = [3.5,1.8,5.0],[8.0,0.9,8.0],[2.6,0.7,2.7]

G_liver = G0 + R * T * math.log(liver[1] * liver[2] / liver[0])
G_muscle = G0 + R * T * math.log(muscle[1] * muscle[2] / muscle[0])
G_brain = G0 + R * T * math.log(brain[1] * brain[2] / brain[0])
max = max(G_liver,G_muscle,G_brain)

print('Results: (kJ/mol)')
print('Liver:',G_liver)
print('Muscle:',G_muscle)
print('Brain:',G_brain)
print('Max:',max)


# 1.2
# Parameter Initialization
# 上接1.1的内容
par = 4.184

G_liver = G_liver / par
G_muscle = G_muscle / par
G_brain = G_brain / par

print('Results: (kcal/mol)')
print('Liver: ',G_liver)
print('Muscle:',G_muscle)
print('Brain: ',G_brain)


# 1.3
proton = 0.000003162
pH = -math.log10(proton)
print('Concentration of proton: ',proton)
print('pH: ','%.3f' %pH)


# 1.4
interval = 20
time = 60 * 6
generation = time / interval
n_Ecoli = math.pow(2,generation)
print('The number of E.coli after 6h is', str(n_Ecoli) + '.')


# 1.5
height = 2e-6
diameter = 5e-7
volume = (diameter / 2) * math.pi * height
print('The volme of E.coli is', str(volume) + '(m3).')


# 2.1
# https://www.ncbi.nlm.nih.gov/protein/O14746.1?report=fasta
telemerase_pro = '''MPRAPRCRAVRSLLRSHYREVLPLATFVRRLGPQGWRLVQRGDPAAFRALVAQCLVCVPWDARPPPAAPS
                    FRQVSCLKELVARVLQRLCERGAKNVLAFGFALLDGARGGPPEAFTTSVRSYLPNTVTDALRGSGAWGLL
                    LRRVGDDVLVHLLARCALFVLVAPSCAYQVCGPPLYQLGAATQARPPPHASGPRRRLGCERAWNHSVREA
                    GVPLGLPAPGARRRGGSASRSLPLPKRPRRGAAPEPERTPVGQGSWAHPGRTRGPSDRGFCVVSPARPAE
                    EATSLEGALSGTRHSHPSVGRQHHAGPPSTSRPPRPWDTPCPPVYAETKHFLYSSGDKEQLRPSFLLSSL
                    RPSLTGARRLVETIFLGSRPWMPGTPRRLPRLPQRYWQMRPLFLELLGNHAQCPYGVLLKTHCPLRAAVT
                    PAAGVCAREKPQGSVAAPEEEDTDPRRLVQLLRQHSSPWQVYGFVRACLRRLVPPGLWGSRHNERRFLRN
                    TKKFISLGKHAKLSLQELTWKMSVRDCAWLRRSPGVGCVPAAEHRLREEILAKFLHWLMSVYVVELLRSF
                    FYVTETTFQKNRLFFYRKSVWSKLQSIGIRQHLKRVQLRELSEAEVRQHREARPALLTSRLRFIPKPDGL
                    RPIVNMDYVVGARTFRREKRAERLTSRVKALFSVLNYERARRPGLLGASVLGLDDIHRAWRTFVLRVRAQ
                    DPPPELYFVKVDVTGAYDTIPQDRLTEVIASIIKPQNTYCVRRYAVVQKAAHGHVRKAFKSHVSTLTDLQ
                    PYMRQFVAHLQETSPLRDAVVIEQSSSLNEASSGLFDVFLRFMCHHAVRIRGKSYVQCQGIPQGSILSTL
                    LCSLCYGDMENKLFAGIRRDGLLLRLVDDFLLVTPHLTHAKTFLRTLVRGVPEYGCVVNLRKTVVNFPVE
                    DEALGGTAFVQMPAHGLFPWCGLLLDTRTLEVQSDYSSYARTSIRASLTFNRGFKAGRNMRRKLFGVLRL
                    KCHSLFLDLQVNSLQTVCTNIYKILLLQAYRFHACVLQLPFHQQVWKNPTFFLRVISDTASLCYSILKAK
                    NAGMSLGAKGAAGPLPSEAVQWLCHQAFLLKLTRHRVTYVPLLGSLRTAQTQLSRKLPGTTLTALEAAAN
                    PALPSDFKTILD'''

aa = 'GAVLIMPSTCNQDERKHFYW'
n = {}
max = 0

for i in range(len(aa)):
    n[i] = telemerase_pro.count(aa[i])
    print(aa[i],'-',n[i])
    if n[i] > max:
        max = n[i]
        max_index = i

print('Max:',aa[max_index],'-',max)


# 2.2
seq = '''AAAACCCGGT'''
base = 'ATGC'
n = {}

for i in range(len(base)):
    n[i] = seq.count(base[i])
    print(base[i],'-',n[i])


# 2.3
insulin = 'CCCHAJEAFIELAKJNFVLAIFEJLIFEJDCCCEFLEFJ'
print(len(insulin))
for i in range(1,len(insulin)):
    print('The former',i,'seqences:',insulin[0:i])


# 2.4
# 区别：前者会自动换行；后者取消换行，直接后接输出
insulin = 'CCCHAJEAFIELAKJNFVLAIFEJLIFEJDCCCEFLEFJ'
aa = 'GAVLIMPSTCNQDERKHFYW'

for i in range(len(aa)):
    n = insulin.count(aa[i])
    print(aa[i],'-',n)

for i in range(len(aa)):
    n = insulin.count(aa[i])
    print(aa[i],'-',n,end = '')



# 2.5
# 选择for循环结构，用string内置函数count实现字符计数。
# 原因：在二者时间复杂度相同的情况下，该方式代码更加简单，节省编程时间



# Part II

# Parameter Initialization
count = 0
base_dic = {'A':0, 'T':0, 'G':0, 'C':0}
baseVar = 'ATCG'

# Base Count
for line in open('yeast_gene.fa','r'):
    if line[0] != '>':
        count = count + len(line) - 1  # substrate the '\n'
        for j in range(len(baseVar)):
            base = baseVar[j]
            base_dic[base] = base_dic[base] + line.count(base)

print('Bases number:',count)
print('Base number:',base_dic)
print('The content of GC:',base_dic['G'] + base_dic['C'])
percent = (base_dic['G'] + base_dic['C']) / count * 100
percent = '%.2f' %percent
print('The percent of GC:',str(percent) + '%')


