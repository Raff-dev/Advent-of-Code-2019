def check_for_criteria1(array):
	double_flag=False
	not_decreasing_flag=True
	for i in range(len(array)):
		if i >0:			
			if array[i-1]==array[i]:
				double_flag=True
			if array[i-1]>array[i]:
				return False				
	return (double_flag)

def check_for_criteria2(array):
	i=0
	thats_a_double=0
	previous_double=False
	memory=-1
	while i<len(array):
		if array[i]>array[i+1] or memory>array[i]:
			return False
		if array[i]==array[i+1]:
			thats_a_double+=1
			if array[i]==memory:
				if previous_double:
					thats_a_double-=1
				thats_a_double-=1
			memory=array[i+1]
			previous_double=True
		elif array[i]==memory:
			if previous_double:
				thats_a_double-=1
			else:
				thats_a_double+=1
			memory=array[i+1]
			previous_double=False			
		else:
			memory=array[i+1]
			previous_double=False
		i+=2		
	return (thats_a_double>0)

def increment(array):
	for i in range(len(array)):
		i+=1
		array[-i]+=1
		if array[-i]==10:
			array[-i]=0
		else:
			return False

def run(array):
	meeting_cryteria=0
	for _ in range(password_max-password_min):
		if check_for_criteria2(array):
			meeting_cryteria+=1
			print(password)
		increment(password)
	print(meeting_cryteria)

password=[2,3,4,2,0,8]
password_min=234208
password_max=765869

run(password)



		
