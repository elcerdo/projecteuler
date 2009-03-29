
aa=2
for x in xrange(1,1000):
    aa*=2

bb=0
aa=str(aa)
for cc in aa:
    bb+=int(cc)

print bb
