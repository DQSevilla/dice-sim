#program to, given a number n representing the number of sides of a die, gives the expected number of coin flips needed
#to simulate rolling said n-sidded die

memoize={1:0}

def e_flips_sim(n):

	if n in memoize:
		return memoize[n]

	if n%2 == 0:
		return 1+e_flips_sim(n//2)
	else:
		return (((n+1)/n)*e_flips_sim(n+1))

def helper(i):
	val=e_flips_sim(i)
	memoize[i]=val
	return val

for i in range(2,101):
	print(str(i)+" -> "+str(helper(i)))
	print(memoize[i])
	print("\n")

print(memoize)