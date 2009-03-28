
ff=[1]
current=1
for k in xrange(1,101):
    current*=k
    ff.append(current)

def cnr(n,r):
    return ff[n]/(ff[r]*ff[n-r])

values=[]
for n in xrange(1,101):
    for r in xrange(n+1):
        aa=cnr(n,r)
        if aa>1e6: values.append(aa)

print len(values)
