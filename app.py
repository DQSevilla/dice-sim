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

full=[]
for subset in itertools.permutations(primelist, len(primelist)):
    full.append(subset)

#print(set(full))
full2=[]
for i in range(0, len(full)):
    for L in range(0, len(full[i])+1):
      for su in itertools.combinations(full[i], L):
        full2.append(su)

print(set(full2))