
primes=[2,3]
def is_prime(k):
    for prime in primes:
        if k%prime==0:
            return False
    return True

for x in xrange(5,100000000):
    if is_prime(x): primes.append(x)
    if len(primes)>10000: break

print len(primes),primes[-1]
