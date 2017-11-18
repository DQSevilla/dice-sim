def findeflips():
	file = open("minflips","r") 
	strings=file.readlines()
	for i in strings:
		if "$2:" in i:
			print(float(i.split(":")[2]))
			break
	
	file.close()

findeflips()