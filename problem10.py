
primes=[2,3]
def is_prime(k):
    for prime in primes:
        if k%prime==0:
            return False
    return True

product=2+3
for x in xrange(5,2000000):
    if is_prime(x):
        print x
        primes.append(x)
        product+=x

print product
