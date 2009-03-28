def valid_triplet():
    for a0 in xrange(1,1000):
        for a1 in xrange(a0,1000):
            a2=1000-a0-a1
            if a2>1:
                triplet=[a0,a1,a2]
                triplet.sort()
                yield triplet

for a,b,c in valid_triplet():
    if a*a+b*b==c*c: print "found %d,%d,%d %d" % (a,b,c,a*b*c)

