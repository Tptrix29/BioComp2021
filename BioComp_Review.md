## BioComp Review

### Shell

#### Command Line

```shell
# Basics
pwd # user info
cd
man
pico # editor

# View File 
more
less
head -n
tail -n 


# Process & Job Control
## What is job or process?
# job: command in shell
# process: running mission after shell parsing
# a job could fork into many processes

# Process running modes
foreground # 前台运行，结束时返回命令结果
background # 挂后台运行, restart a job in bg: & [job number]
bg # 挂后台暂停, = ctrl + Z

# job control
jobs -l # current session jobs
ps -l # current running process
ctrl + C # kill foreground job
fg %n # 后台到前台, n--job number
bg %n # run recent stopped job
kill %n # kill job
kill -9 [PID] # kill process


# Common command
ls
mkdir
rm -r # recursively delete
rm -f # delete file
mv # rename or move
cp
touch

# User permission
# u(owner), g, o
# r(4), w(2), x(1)
chmod [] [filename]
-R # recursively

# Pipe
> # output, fully new
>> # append
< # input
| # pipe

# Alias
alias
unalias

# Other useful command
# tr, translate characters
# read from stdin
# Syntax: tr [-cds][string1][string2]
-d # delete
-c # oppsite operation
-s # squezze successive repeats
# e.g.
tr -c a s  # not "a" -> "s"
a
as # change "\n" into "s"

# wc, counting result
-l # count line
-w # count word
-c # count char

# cat, concatenate

# cut, select columns
-f [colList] # e.g. 1-5 or 2,3,6
-c [posList] # position of line
-d [sperator] 

# paste, join columns

# sort, sort line
-t # seperator
-n # numeric order, value, not first char
-r # reverse, default: ascending(1-9)
-k # key
-o [output filename]

# uniq, list unique item
-c # each line with occurance count, count num is concatenate with fisrt column
-d # write duplicated lines
-u # wirte unique line
```



#### Regular Expressions

```shell
# grep command

# Regex Basics
. # any char
[] # char set
[^] # negated char
^ # beginning
$ # end
* # >=0 occurance
+ # >=1 occurence
? # 0 or 1 occurence

\{n,m\} # repeat range
\( \)\{n,m\} # subexpression 
(T|F) # 'Or'

# Backreference
# Syntax(backreference specifier): \n, n is number
# backreference context should be enclosed by \(\)
# Examples:
# ^\([[:alpha:]]\{1,\}\).*\1$ 
# 
# \(['`]\).*\1
# 


# Special set
# Example: [45[:alpha:]] == [45a-zA-Z]
alpha # [a-zA-Z]
lower
upper
alnum # [0-9a-zA-Z]
digit # [0-9]
punct # punctuations
space # whitespace char, including space, tab, NL, FF, VT, CR

# Metacharacters
\b # word boundary
\B # not word boundary
\d # digit
\D # non-digit
\f # next page
\n # newline character, move to begining of next line
\r # carraige return character, return to beginning of local line
\t # tab
\v # vertical tab
\s # whitespace, = [\f\n\r\t\v]
\S # non-whitespace
\w # word char, (alnum + _) , = [a-zA-Z0-9_]
\W # non-word char

```



#### grep

```shell
# global regular expression print
# Family:
# grep--regex
# fgrep--not regex
# egrep--extended grep, use more powerful set, no backreference, fastest
# Syntax: grep--BREs, egrep--EREs
# Regex should be enclosed with ""

# Options:
-c # print count of matched
-i # ignore uppercase or lowercase
-n # print line number and line context of match
-l # print filename match
-h # print match lines
-v # print match oppsite
-e # regex pattern
-E # extended regex pattern
-o # print only match part

# Usage accompany with wc
# Notice: consider \n when counting
```



#### sed

```shell
# Syntax: 
# sed [-e command][-f filename][-n]
# -n: print only specific processed context

# s: substitute, s/pattern/replacement/[matching model]
# Matching model:
# n: int number, indicating the number of occurance
# g: global
# p: print pattern
# Replacement pattern:
# &: entire matched string  e.g. 
# \n: nth substring, = \(\)
# \: escape character, 转义字符
# e.g.
head -n 10 /etc/passwd | sed -e '3,$d'  # delete 3～last line

# a: append, 后
# i: insert, 前
# c: change
# d: delete
# p: print
# y: transform
# q: quit
# e.g.
head -n 10 /etc/passwd | sed -e '2i\   
hello world!\'
head -n 10 /etc/passwd | nl | sed -e '/^$/, $p'
```



#### awk (prior to sed)

```shell
# C-like syntax
# Regex enclosed with //
# e.g.
awk '
BEGIN { print "List:"}
/\.html$/ { print }  # print matched context
END {print "Done.\n" "Bye~" }
'
# print notcies:
# concatenate with space char: print [str1], [str2] 
# concatenate directly: print [str1] [str2]

# Seperator
# Default: \n
# RS, change row seperator

# NR, current record num

# Fields
# FS, field seperator, default is whitespace
# awk -F [field seperator]
# $0, full line
# $n, nth field
# NF, number of field
# field match: $2 ~ /TJU/

# Other Support
# Logical calculation
# Loop control
# Array and Dictionary

# Built-in funcitons
# Arithmetic: sin, cos, atan, exp, int, log, rand, sqrt
# String: length, substr(子字符串), split
#    substr(string, start site, substr length)
#    split(string, result array name, seperator)
# Output: print, printf
# Special:
# system("[command line]")
# exit, immediately move to END
```



#### Shell Variables

```shell
# Environment and Variables
$PATH
$SHELL
$HOME

# Configure file
# .bashrc or .bash_profile

# Variables
export # change variable, 不改变原值
unset varname 
# e.g.
a='hello' # NO a = 'hello', ERROR!
echo $a

# NOTICE!!!
# Shell variable always char!!!
# Cautions for numeric operation!!!
```



#### Shell Script

```shell
# Script beginning: #!/bin/bash
# indicate running shell

# Running: bash [script file]

# Calculation command: expr
# Seperate by space character
# Logical operator: | or &
# e.g.
# val=`expr 1 + 3`

# for loop
# e.g. output all filenames
#!/bin/bash
for i in *
do
	echo $i
done
# list
#!/bin/bash
for i in 1 7 9
do
	echo $i
done

# if control
# test: -eq, -ne, -lt, -gt, -le, -ge
# test: -f(file), -d(dierctory), -x(excutable), -s(longer than 0 bytes)
# alias: []
# e.g.
#!/bin/bash
i=9  # the '=' char must not be enclosed by space char!!! (Syntax Error)
if test $i -eq 9
then
	echo `expr 1 + 1`
elif test $i -eq 8
then
	echo $i
else
	:  # Null script
fi

# until loop
# e.g.
#!/bin/bash
x=1
until [ $x -gt 3 ]
do 
	echo $x
	x=`expr $x + 1`  # expr 4 \* 6, 转义
done

# Debugging
# Command: sh
# Options: 
-n # Syntax examine without excution
-v # display script line when excuted
-x # display command and arguments when excuted

# Running environment
$0 # script name
$# # total parameter number
$@ # whole parameter
$n # nth parameter

# Integer Calculation
# $(())

# Command line running 
# `[command line]`

# “” & ‘’
# 双引号：弱引用
# 单引号：强引用，原样输出
```



### Python

#### Basics

```python
# Module import
import math
from math import *

# Comments
# comments or
'''
comments
'''

# for loop
import random
for i in range(10):
  index = random.randint(0, 5)
  print(index)
 
# while loop
sum = 0
i = 1
while i <= 100:
  sum += i
  print(sum)
  i += 1

# if statement
if a == 0:
  print(0)
elif a < 0:
  print("negative")
else:
  print("positive")

  
# Logical calculation 
and, &
or, |
not
!=
```



#### Data Structure

```python
# Numeric
int()
float()

# List
list.append(element) # as one element
list.extend() # 展开
list.pop(index) # remove one element
list.remove(element)
del(list[index])

# Tuple
tuple() # can't be changed

# String
str()
str.split()[1].strip()

# Dictionary
dic = {"a": 'numeric', "b": 'program'}
dic.keys()
dic.values()
dic.pop(key)
del dic[key]

# Set
s1 = set('Python')
s1.add('R') # 1 element
s1.update(list) # add list
# remove element
s1.pop()
s1.remove(element)
s1.discard(element)
# Set membership
s1 = set([1,2,3,4,5,10])
s2 = set([10,4,5])
s1.issubset(s2)
>> False
s1.issuperset(s2)
>> True

```



#### Tabular Data

```python
# list of lists ***
# dic of dics
# Mixed list and dic

# 
enumerate(list_x) # tuples(i, x[i])
# e.g.
for index, line in enumerate(open('open.txt', 'w')):
	pass
reduce(fun, list/tuple)
# e.g.
reduce(set.insertation, tuple_set)  # iteration

# set difference
old = set()
new = set()
new.difference(old)
new.symmetric_difference(old)

# column access
zip(*table) # transpose tables
# e.g.
table = [[2, 4], [4, 6], [7, 7]]
for i in zip(table):
  print(i)
>>([2, 4],)
>>([4, 6],)
>>([7, 7],) 
print(*table)
>>[2, 4] [4, 6] [7, 7]
for i in zip(*table):
	print(i)
>>(2, 4, 7)
>>(4, 6, 7)

# list operation
[1, 4, 5] + [4, 7]
[4, 5] * 3 # [4, 5, 4, 5, 4, 5]

# Sort table
from operator import itemgetter
sorted_table = sorted(table, key = itemgetter(column_num), reverse = True) # descending
list.sort()
```



#### Text Mining

```python
# Regex
# match()
import re
pattern = re.compile('[SQ]A')
match = pattern.search(seq)
match.start(), match.end() # 左开右闭
match.group() # match string
match.span() # tuple

# findall()
import re
motif = 'R.[SA][^P]'
regex = re.compile(motif)
total = regex.findall(seq) # list

it = regex.finditer(seq)
for s in it:
  print(s.group()) # s--Match object
  print(s.group(2)) # match list index

# subgroup
p = re.compile('(a(b)c)d')
m = p.match('abcd')
m.group(0)
>> "abcd"
m.group(1)
>> "abc"
# ?P<w1>
pattern = 'R(?P<w1>.{0,2})[ST](?P<w2>[^P])'
regex = re.compile(pattern)
m1 = regex.search(seq)
m1.group('w1')

# Modify string
re.split(pattern, str)  # seperator = re.complie(pattern) / r'[pattern]'
re.sub(pattern, replace, str)  # 返回替换后内容
re.subn(pattern, replacement, str)  # 返回tuple(替换后内容, 替换次数)

# Some Modules
# urllib
import urllib
handler = urllib.request.urlopen(url)
html = handler.read().decode('utf-8')

# struct, bytes <-> tuple
import struct
format = '2s1s1s1s1s'
a = struct.pack(format, b'10', b'2', b'3', b'40', b'9')
line = '123456'
b = struct.unpack(format, line.encode('utf-8'))

# Encode & Decode
# bytes
b = bytes("中国", encoding = 'utf-8')
s = b.decode("utf-8")
```



#### Function & Class

```python
# Function
def fun1(pars, *args):
  print(args) # tuple, except pars
  return None
# lambda function
g = lambda x: x ** 2
print(g(8))
>> 64

# Class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
		
    # self description
    # calleb by "print(person)""
    def __repr__(self): 
        return 'Name: %s' % self.name

    def show(self):
        print(self.name)


class Student(Person):
    def __init__(self, name, age, stID):
        Person.__init__(self, name, age)
        self.ID = stID

    def show_id(self):
        print(self.ID)
        print(self.name)

if __name__ == '__main__':
  pass

```



#### Error Debug

```python
# Error type(examples)
SyntaxError
FileNotFoundError
NameError
ModuleNotFoundError
ValueError
IndexError

# try
try: 
  # statements
except ValueError:
  # statements
  raise ...
else:
  # statements
```



#### Program Pipeline

```python
import os
os.system(commandline)
os.path.exist()
os.listdir()
os.chdir()
os.getwd()
os.remove()


import sys
sys.argv[index]  # python script.py(0) argv1(1) argv2(2)
```



### R

#### Basic

```R
# Keyboard shortcut
# Ctrl + U, delete command
# Ctrl + C, intertupt running computation without terminate R
# Tab, automaticly fill


# Get Help
help(functioname)
?functionname
args(functionname)
??pattern
help.search("pattern")
help(package = 'packagename')
vignette()
# ......


# working directory
getwd()
setwd(workpath)

# Save workspace
save.image() # .Rdata

# History
hitory()

# Loaded Package Search
search()

# Package
# Load
library()
require()
# Unload
detach()
# Install
install.packages("")

# Running script
source()

# print
# only one object!
print('a value is');print(a);print(".")

# Variable setting
# <- or =

# List variables
ls()

# Delete variables
rm()

# Create vector
c()

# Basic statistics
mean()
median()
sd()
var()
cor() # correlation
cov() # covariance

# Sequence
seq(from = 0, to = 20, by = 2)
seq(from = 0, to = 20, length.out = 5)

# Logical computation
# AND: &
# Or: |

# Digits: 小数点位数
# para: digits = n

# Output redirecting
sink(filename)
source()
sink()

# List files
list.files(recursive = T, all.files = T)

# Read table
read.table()
read.csv()

# Write table
write.csv()

# MySQL Databases
# Package: RMySQL
library(RMySQL)
con = dbConnect(MySQL(), user = 'gemo', password = 'password',
               dbname = 'hg19', host = 'genome-mysql,.cse.uscs.edu')
dbListTabels(con)
sql <- "SELECT * from refGene"
refGene <- dbGetQuery(con, sql)
dbDisconnect(con)

# Numeric Tip
8 %% 2  # 求余
```



#### Data Structure

```R
# Vectors
# List
# Scalar
# Matrice
# Array  3+ dimension
# Factors, unique--level
# DataFrame

# Physical type
mode() # store in memory
# Abstract Type
class()

# insert data into vector
append(v1, insert, after = append site)

# df and vector append
cbind()

factor(vector, [levels order])
levels()

stack(list(fresh = freshman, score = grade)) # list -> df, column combination

list()
listname[["test"]] <- NULL  # remove

# matrix
mat <- matrix(Data, nrow, ncol, byrow = TRUE) 
t(mat)  # transposition
solve(mat)  # inverse
A %*% B  # matrix multiply
A * B  # element multiply
diag(n)  # n-dimension identity matrix
mat[] # select

# DataFrame
data.frame()
sample(vector, n, replace = TRUE) # 放回抽样
rbind() # append row
df$colname # select
subset(df, select = c(colname), subset = (cond)) # select
na.omit(df) # remove NA
cbind() # column combination
merge(df1, df2, by = colname) # join data
with(df, [col operation]) # apply on each col
attach(df) # insert into search list

# data type convertion
as.character()
as.complex()
as.numeric(), as.double()
as.integer()
as.logical()

as.list()
as.data.frame()
as.matrix()
as.vector()

# group, return a list of vec
split(vector, factor)  # factor--colname
unstack(data.frame(vec, factor))

# apply
lapply(list, fun) # return list
sapply(list, fun) # return vector
apply(mat, 1/2, fun) # 1-row, 2-col
tapply(x, f, fun) # group data, then apply function
by(df, factor, fun) # group row, factor--colname
mapply(fun, vec1, vec2, ..., vecn) # element

# Common function
length(vec)
nchar(str)
dim(df/mat)
paste("hello", "world", sep = ' ') # concatenate string
substr(str, start, end)
strsplit(str, seperator)
sub(old, new, str) # first
gsub(old, new, str) # global
# all combination
outer(mat1, mat2, paste, sep = '-')

# System
Sys.Date()
as.Date("12/3/2010", format = "%m/%d/%Y")
format(Sys.Date(), format = "%m/%d/%Y")
# format
%b # Abbreviated month name
%B # Full month name
%d # two-digit month
%m # two-digit number
%y # year without centry(0-99)
%Y # year with centry
ISOdate() # POSIXct object

```

#### Probability and Statistics

```R
# Names
dnorm() # density
pnorm() # probability distibution, P(X <= x)
qnorm() # quantile
rnorm() # random value consistent with probability distibution

# Discrete Distribution
binom(n, p)
geom(p)
hyper(nwhite, nblack, nselect)
nbinom(size, p/mu) # Negative binominal distribution
pois(lamnda)
beta(shape1, shape2)
cautchy(location, scale)
chisq(degree)
exp(rate)
f(dg1, dg2)
gamma(rate/scale)
lnorm(mean) # Log-nominal
logis(loc, scale) # logistic 
norm(mean, sd) 
t(df)
unif(min, limit, max) 
weibull(shape, scale) # Weibull
wilcox(m, n) # Wilcoxon

choose(n, k) # combination number
combn(vector, n)

set.seed() # seed for random num

# Some plot
abline(height) # line
polygon(xrange, yrange, density)

summary(df)
mean(vec < 5)
table(factor1, factor2)
summary(table(ini, out)) # independency test
quatile(vec, precent)
scale() # to z-score

# Statistics Tests
# Mean test
t.test(x, mu = m)
# Proportion test
prop.test(x, n, p)
# Normality test
shapiro.test(x) # n <= 5000
# Runs test, binary data random?
library(tseries)
runs.test(as.factor(s))
# Means Comparison 
t.test(x, y)
# Location Comparison
wilcox.test(x, y)
# Correaltion significance test
cor.test(x, y)
# Group for equal proportion
prop.test(vec1, vec2)
# Same distribution test
ks.test(x, y)
```



#### Graphics

```R
# Scatter
plot(x, y, main = name, xlab = str1, ylab = str3, 
     xlim = [1, 2], ylim = [2, 4], type = 'n') 
# 'n'--initialize without plot, points over line, 'l'--plot line, 'o'--scatter

grid()
points() # overlaid
lines() # overlaid
plot(x, y, pch = as.integer(f)) # point type

# Multiple groups
par(mfrow/mfcol = c(1, 2))  # fill graghs by row or column
with(df, plot(col, col))
with(df, plot(col, col))

# Legend
legend(x, y, labels, pch, lty, lwd, col)

# Linear regression
m <- lm(y~x)
plot(y~x)
abline(m)

coplot(y~x|f) # each factor level

# Bar plot
bar(vec, col)
# confidence intervals
library(gplots)
barplot2(vec, plot.ci = T, ci.l = lower, ci.u = upper, names.arg = vec)

# Boxplot
boxplot()

# Histogram
hist(x, prob = F)

# Esitimate Density
density()
lines(density(samp))

table() # count occurrence

# Q-Q plot
qqnorm()
qqline()

curve()

par(ask = T) # Ask for each plot
```



#### R Programming

```R
# if statement
if (cond1) {
  commands
} else if (cond2) {
  commands
} else {
  commands
}

# for loop
for (i in vec) {
  commands
}

# while loop
while (cond) {
  commands
}

# repeat loop
repeat {
  commands
  if (cond) {
    break
  }
  commands
}

# Functions
funname <- function(pars){
  body
  returnName
}

# Speed Comparison
system.time(command)

# Robust ANOVA
kruskal.test(x ~ f)

# Principal Component Analysis, PCA
r <- prcomp(x)
print(r)

# Clustering 
d <- dist(x)
hc <- hclust(d)
clust <- cutree(hc, k = n)

# Linear Regression
lm()
# Statistics
anova()
coef()
deviance() # residue sum
effects() # vec of orthogonal effects
fitted() # fitted y value
residuals() 
summary()
vcov() # variance-covariance matrix
plot() # residual vs fit, normal Q-Q, scale-location, residual vs leverage

# Logistic regression
m <- glm(x ~ y, family = binomial, data = dateset)
predict(m ,type = 'response', newdata = df)
```
