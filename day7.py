from itertools import *
def diagnostics(mem,phase,phase_index,adress,id_input):
	#print(phase_index,adress)
	mode=[0 for _ in range(max(5,len(str(mem[adress]))))]
	opcode=int(str(mem[adress])[-2:])
	assert opcode in {0,1,2,3,4,5,6,7,8,99}
	for i in range(len(str(mem[adress]))-2):
		mode[i]=(int(str(mem[adress])[-i-3]))
	if opcode == 1:
		mem[ea(mem,mode,adress,3)]=mem[ea(mem,mode,adress,1)]+mem[ea(mem,mode,adress,2)]
	elif opcode == 2:
		mem[ea(mem,mode,adress,3)]=mem[ea(mem,mode,adress,1)]*mem[ea(mem,mode,adress,2)]
	elif opcode == 3:
		mem[ea(mem,mode,adress,1)]=id_input if flag[phase_index] else phase[phase_index]
		flag[phase_index]=True
	elif opcode == 4:
		outputs.append(mem[ea(mem,mode,adress,1)])
		adress+=2
		amp_adress[phase_index]=adress
		if phase_index==4 and phase[phase_index] in {0,1,2,3,4}:
			return outputs[-1] 
		elif phase_index==4:
			return diagnostics(amp_mem[0],phase,0,amp_adress[0],outputs[-1])
		return diagnostics(amp_mem[phase_index+1],phase,phase_index+1,amp_adress[phase_index+1],outputs[-1]) 
	elif opcode == 5 and mem[ea(mem,mode,adress,1)]:
		adress=mem[ea(mem,mode,adress,2)]
	elif opcode == 6 and not mem[ea(mem,mode,adress,1)]:
		adress=mem[ea(mem,mode,adress,2)]
	elif opcode == 7:
		mem[ea(mem,mode,adress,3)]=int((mem[ea(mem,mode,adress,1)]<mem[ea(mem,mode,adress,2)]))
	elif opcode == 8:
		mem[ea(mem,mode,adress,3)]=int((mem[ea(mem,mode,adress,1)]==mem[ea(mem,mode,adress,2)]))
	elif opcode == 99:
		return outputs[-1]
	else:
		adress+=3
	adress+=2 if opcode in {3,4} else 0
	adress+=4 if opcode in {1,2,7,8} else 0
	return diagnostics(mem,phase,phase_index,adress,id_input)
	
def ea(mem,mode,adress,offset):#effective adress
	return mem[adress+offset] if mode[offset-1] == 0 else adress+offset

def Answer(phase_set):
	global amp_adress,flag,amp_mem
	for phase in permutations(phase_set,5):
		for i in range(5):			
			amp_adress[i]=0
			amp_mem[i]=memory.copy()
		flag=[0,0,0,0,0]
		yield diagnostics(memory.copy(),list(phase),0,0,0)

memory = [3,8,1001,8,10,8,105,1,0,0,21,38,63,72,81,106,187,268,349,430,99999,3,9,101,5,9,9,1002,9,3,9,101,3,9,9,4,9,99,3,9,102,3,9,9,101,4,9,9,1002,9,2,9,1001,9,2,9,1002,9,4,9,4,9,99,3,9,1001,9,3,9,4,9,99,3,9,102,5,9,9,4,9,99,3,9,102,4,9,9,1001,9,2,9,1002,9,5,9,1001,9,2,9,102,3,9,9,4,9,99,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,99,3,9,1001,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,99]
amp_adress={}
amp_mem={}
outputs=[]
print('Answer 1:',max(Answer([0,1,2,3,4])))
print('Answer 2:',max(Answer([5,6,7,8,9])))

#1474258
