#program to, given a number n representing the number of sides of a die, gives the expected number of coin flips needed
#to simulate rolling said n-sidded die

def all_factors(num):
    ret=[]
    for i in range(2,num):
        if(num%i==0):
            ret.append(i)
    return ret

memoize={1:0}

def e_flips_sim(n):
	if n in memoize:
		return memoize[n]

	if n%2 == 0:
		return 1+flip_helper(n//2)
	else:
		factors=all_factors(n)
		poss_min=(((n+1)/n)*flip_helper(n+1))
		
		i=n
		while not (i and (not(i & (i - 1)))):
			i=i+1

		for i in range(n+2,i+1):
			val=(i/n)*flip_helper(i)
			if poss_min>val:
				poss_min=val

		for i in factors:
			val=(flip_helper(i)+flip_helper(n//i))
			if poss_min>val:
				poss_min=val
		return poss_min

def flip_helper(i):
	val=e_flips_sim(i)
	memoize[i]=val
	return val

for i in range(1,1025):
	var=flip_helper(i)
	print(str(i)+" -> "+str(var))
#print(memoize[i])
print("\n")

#f_out=open("lot_of_flips.txt","w+")
#f_out.write(str(memoize))
#f_out.close()
#print(memoize)
