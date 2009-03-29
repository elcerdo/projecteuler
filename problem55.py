
cache={}
def is_lychrel(n,iter=0):
    if n in cache:
        return cache[n]

    if n<10:
        cache[n]=False
        return False

    if iter>53:
        cache[n]=False
        return False

    bb=""
    for char in reversed(str(n)):
        bb+=char
    bb=int(bb)

    aa=n+bb

    if is_palindrome(aa):
        cache[n]=True
        return True
    else:
        value=is_lychrel(aa,iter+1)
        cache[n]=value
        return value

def is_palindrome(n):
    aa=str(n)
    if len(aa)<2: return False

    direct=iter(aa)
    revers=iter(reversed(aa))
    try:
        while True:
            if direct.next()!=revers.next(): return False
    except StopIteration:
        return True

results=[]
for n in xrange(10,10000):
    if not is_lychrel(n): results.append(n)
print len(results)
