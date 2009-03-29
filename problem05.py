primes={2:0,3:0,5:0,7:0,11:0,13:0,17:0,19:0}


def update_factor(k):
    global primes
    for prime in primes:
        kk=k
        ll=0
        while kk%prime==0:
            ll+=1
            kk/=prime
        if primes[prime]<ll: primes[prime]=ll

for k in xrange(1,21):
    update_factor(k)

aa=1
for prime,factor in primes.items():
    aa*=prime**factor
print aa
