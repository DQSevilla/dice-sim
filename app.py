import itertools

def primes(n):
    primfac = []
    d = 2
    while d*d <= n:
        while (n % d) == 0:
            primfac.append(d)
            n //= d
        d += 1
    if n > 1:
       primfac.append(n)
    return primfac

number=input()

primelist=primes(int(number))

import itertools
for subset in itertools.permutations(primelist, len(primelist)):
    print(subset)