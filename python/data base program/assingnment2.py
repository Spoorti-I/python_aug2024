def check_arrangement(boy_heigts, girl_heigts):
	for i in range(1, len(boy_heigts)):
		if boy_heigts[i] < girl_heigts[i-1] or girl_heigts[i] < boy_heigts[i-1]:
			return 'No'
	return 'Yes'

T=int(input('Number of test cases'))

arrangement = []
for i in range(T):
	 N (number of boys or girls)
	N boys heights boy_heigts[]
	Read N girls heights girl_heigts[]
	
	sort boy_heigts
	sort girl_heigts
	
	arrangement.append( check_arrangement(boy_heigts, girl_heigts) )

print arrangement
