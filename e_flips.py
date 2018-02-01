#program to, given a number n representing the number of sides of a die, gives the expected number of coin flips needed
#to simulate rolling said n-sidded die

memoize={1:0}

def e_flips_sim(n):

	i=2**(n - 1).bit_length()

	if n in memoize:
		return memoize[n]	

	# if n==2:
	# 	return 1

	#print(str(n))

	if n%2 == 0:
		return 1+e_flips_sim(n//2)
	else:
		l=float('inf')
		for m in range(n+1,n+2):
			res=((m/n)*e_flips_sim(m))
			if l>res:
				l=res
		return l

def helper(i):
	return memoization(i,e_flips_sim(i))

def memoization(key,value):
	memoize[key]=value
	return value

def isPow2(i):
	return (i and (not(i&(i-1))))

for i in range(2,10001):
	print(str(i)+" -> "+str(helper(i)))
	print(memoize[i])
	print("\n")

# for i in range(70,101):
# 	print(str(i)+" -> "+str(helper(i)))
# 	print(memoize[i])
# 	print("\n")

print(memoize)