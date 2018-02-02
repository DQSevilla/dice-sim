number=input()

def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

def superset(arr):
    ret=[[]]
    for i in arr:
        ret=ret+ret
        for j in range(len(ret)//2,len(ret)):
            ret[j]=ret[j]+[i]
    return ret

def all_perms(elements):
    if len(elements) <=1:
        yield elements
    else:
        for perm in all_perms(elements[1:]):
            for i in range(len(elements)):
                yield perm[:i] + elements[0:1] + perm[i:]

def remove_dup(duplicate):
    final_list = []
    for num in duplicate:
        if num not in final_list:
            final_list.append(num)
    return final_list

out=[]

for i in superset(prime_factors(int(number))):
    out+=list(all_perms(i))

print(remove_dup(out))