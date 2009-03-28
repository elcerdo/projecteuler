
aa=1
bb=1
cc=aa+bb
l=3
while len(str(cc))<1000:
    aa=bb
    bb=cc
    cc=aa+bb
    l+=1

print l

