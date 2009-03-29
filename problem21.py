
cache={}
def proper_divisor_sum(n):
    if n in cache:
        return cache[n]
    aa=0
    for k in xrange(1,n/2+1):
        if n%k==0: aa+=k
    cache[n]=aa
    return aa

ok=set()
for n in xrange(1,10000):
    m=proper_divisor_sum(n)
    np=proper_divisor_sum(m)
    if n==np:
        fs=frozenset((m,n))
        if fs not in ok:
            ok.add(fs)

aa=set()
for prout in ok:
    if len(prout)>1: aa.update(prout)

print sum(aa)
