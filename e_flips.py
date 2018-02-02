#program to, given a number n representing the number of sides of a die, gives the expected number of coin flips needed
#to simulate rolling said n-sidded die
exec(compile(open('app.py').read()))

memoize={1:0}

def e_flips_sim(n):

	if n in memoize:
		return memoize[n]

	if n%2 == 0:
		return 1+e_flips_sim(n//2)
	else:
		return (((n+1)/n)*flip_helper(n+1))

def flip_helper(i):
	val=e_flips_sim(i)
	memoize[i]=val
	return val

for i in range(2,101):
	flip_helper(i)
	print(str(i)+" -> "+str(flip_helper(i)))
	#print(memoize[i])
	print("\n")

#f_out=open("lot_of_flips.txt","w+")
#f_out.write(str(memoize))
#f_out.close()
print(memoize)