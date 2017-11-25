def findeflips():
	file = open("minflips","r") 
	strings=file.readlines()
	found=0
	for i in strings:
		i=i.split(":");
		if "4" is i[0]:
			if i[2] is "":
				print("found but empty")
				print("calling function to fill empty spaces with data")
			else:
				print(float(i[2]))
			found=1
			break
	if found is 0:
		print("not there")
		print("calling function to fill text file to that point, then")
		print("calling function to fill empyt spaces with data")
	file.close()

findeflips()