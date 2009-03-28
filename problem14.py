
cache={}
cache[1]=1

def chain(n):
    if n in cache:
        return cache[n]
    elif n%2==0:
        vv=1+chain(n/2)
        cache[n]=vv
        return vv
    else:
        vv=1+chain(3*n+1)
        cache[n]=vv
        return vv

sn=13
ll=chain(13)
for x in xrange(1,1000000):
    lll=chain(x)
    if lll>ll:
        ll=lll
        sn=x

print sn,ll
