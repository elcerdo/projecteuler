
import string

mapping={}
for code,char in enumerate(string.uppercase):
    mapping[char]=code+1

def score(str):
    return sum(mapping[char] for char in str)

cache=set([1,3,6,10,15,21,28,36])
cache_max=36
def is_triangle(n):
    global cache_max
    while cache_max<n:
        nn=len(cache)+1
        cache_max=nn*(nn+1)/2
        cache.add(cache_max)
    return n in cache

file=open("inputs/words.txt")
words=[line.rstrip('\n') for line in file]
file.close()
tris=[word for word in words if is_triangle(score(word))]
print len(tris)
