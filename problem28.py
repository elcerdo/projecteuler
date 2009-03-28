
import scipy as s

m=s.zeros((1001,1001),dtype=s.int0)

def fill():
    aa=s.array(m.shape,dtype=s.int0)
    aa/=2
    state=(1,aa)

    def fill_line(dir,n,(current,pos)):
        for k in xrange(n):
            m[pos[0],pos[1]]=current
            current+=1
            pos+=dir
        return current,pos

    def one_turn(k,state):
        state=fill_line([1,0],2*k-1,state)
        state=fill_line([0,-1],2*k,state)
        state=fill_line([-1,0],2*k,state)
        state=fill_line([0,1],2*k+1,state)
        return state

    state=fill_line([0,1],1,state)
    for k in xrange(m.shape[0]/2):
        state=one_turn(k+1,state)



def compute_sum():
    aa=[m[k,k] for k in xrange(m.shape[0])]
    bb=[m[k,m.shape[1]-1-k] for k in xrange(m.shape[0])]
    return sum(aa)+sum(bb)-1

fill()
print compute_sum()
