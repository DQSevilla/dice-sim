def findeflips():
	file = open("minflips","r") 
	strings=file.readlines()
	found=0
	for i in strings:
		if "$4:" in i:
			if i.split(":")[2] is "":
				print("found but empty")
				print("calling function to fill empty spaces with data")
			else:
				print(float(i.split(":")[2]))
			found=1
			break
	if found is 0:
		print("not there")
		print("calling function to fill text file to that point, then")
		print("calling function to fill empyt spaces with data")
	file.close()

findeflips()