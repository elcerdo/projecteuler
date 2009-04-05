
import scipy as s

file=open("inputs/matrix.txt")
lines=file.readlines()
file.close()

mat=s.array([[int(aa) for aa in line.rstrip('\n').split(' ')] for line in lines],dtype=s.int0)
total=s.zeros(mat.shape,dtype=s.int0)


total[0,0]=mat[0,0]

def updatetotal(i,j):
    nn=[]
    if i>0: nn.append(total[i-1,j])
    if j>0: nn.append(total[i,j-1])
    total[i,j]=mat[i,j]
    if nn: total[i,j]+=min(nn)

for k in xrange(1,mat.shape[0]):
    for l in xrange(0,k+1):
        updatetotal(k-l,l)

for k in xrange(-mat.shape[0]+1,0):
    for l in xrange(k,0):
        updatetotal(total.shape[0]+k-l-1,total.shape[1]+l)

print total[-1,-1]
