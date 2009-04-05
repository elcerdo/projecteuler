
import scipy as s

total=s.zeros((21,21),dtype=s.int0)
total[0,0]=1

def updatetotal(i,j):
    nn=[]
    if i>0: nn.append(total[i-1,j])
    if j>0: nn.append(total[i,j-1])
    total[i,j]=sum(nn)

for k in xrange(1,total.shape[0]):
    for l in xrange(0,k+1):
        updatetotal(k-l,l)

for k in xrange(-total.shape[0]+1,0):
    for l in xrange(k,0):
        updatetotal(total.shape[0]+k-l-1,total.shape[1]+l)

print total[-1,-1]
