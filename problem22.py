
import string

mapping={}
for code,char in enumerate(string.uppercase):
    mapping[char]=code+1

def score(str):
    return sum(mapping[char] for char in str)

file=open("inputs/names.txt")
names=[line.rstrip('\n') for line in file]
file.close()
names.sort()

scores=[(score(name),name) for name in names if name]

prout=0
for k,(score,name) in enumerate(scores):
    prout+=(k+1)*score

print prout
