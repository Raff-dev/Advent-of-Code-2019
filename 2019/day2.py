def intCode(memory,noun,verb):
	memory[1]=noun
	memory[2]=verb
	adress=0
	while memory[adress]!=99:

		if memory[adress] == 1:
			memory[memory[adress+3]]=memory[memory[adress+1]]+memory[memory[adress+2]]

		elif memory[adress] == 2:
			memory[memory[adress+3]]=memory[memory[adress+1]]*memory[memory[adress+2]]
		else:
			#print('Oh noes its broken')
			pass
		adress+=4
	return(memory[0])

def get_memory():
	return [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,13,1,19,1,10,19,23,1,6,23,27,1,5,27,31,1,10,31,35,2,10,35,39,1,39,5,43,2,43,6,47,2,9,47,51,1,51,5,55,1,5,55,59,2,10,59,63,1,5,63,67,1,67,10,71,2,6,71,75,2,6,75,79,1,5,79,83,2,6,83,87,2,13,87,91,1,91,6,95,2,13,95,99,1,99,5,103,2,103,10,107,1,9,107,111,1,111,6,115,1,115,2,119,1,119,10,0,99,2,14,0,0]
print('The answer 1 is ' + str(intCode(12,2)) + '!')

for noun in range(0,100):
	for verb in range(0,100):
		output=intCode(get_memory(),noun,verb)
		if output==19690720:
			print('The answer 2 is ' + str(100*noun+verb))
