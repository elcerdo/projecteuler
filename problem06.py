
aa=0
bb=0
for k in xrange(1,101):
    aa+=k*k
    bb+=k

bb*=bb

print bb-aa
