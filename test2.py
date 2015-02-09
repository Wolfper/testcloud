print ('hello')
def testtrue(money):
    if money:
        print("wow i have money")
    else:
        print("no money")
        
testtrue(0)
testtrue(20)
testtrue(-1)

def pasy(name = None, password = None):
	while not (name and password):
		if not name:
			name = input('podaj imię:')
		elif not password:
			password = input('podaj haslo: ')
	return name, password
	
pasy()