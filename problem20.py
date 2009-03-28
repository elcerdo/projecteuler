
ff=[1]
current=1
for k in xrange(1,101):
    current*=k
    ff.append(current)

prout=str(ff[100])
aaa=0
for digit in prout:
    aaa+=int(digit)

print aaa
