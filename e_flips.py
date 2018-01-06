#program to, given a number n representing the number of sides of a die, gives the expected number of coin flips needed
#to simulate rolling said n-sidded die

def e_flips_sim(n):
	i=n
	while not isPow2(i):
		i=i+1

	if n==2:
		return 1

	if n%2 == 0:
		return 1+e_flips_sim(n//2)
	else:
		l=float('inf')
		for m in range(n+1,i+1):
			if l>((m/n)*e_flips_sim(m)):
				l=((m/n)*e_flips_sim(m))
		return l

def isPow2(i):
	if i<=1:
		if i==1:
			return 1
		else:
			return 0

	return isPow2(i/2)

for i in range(2,100):
	print(str(i)+" -> "+str(e_flips_sim(i)))