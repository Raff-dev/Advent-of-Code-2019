data=open('day8_data.txt').read()
width,height,zcount,count,index,ones,twos=25,6,0,0,0,0,0
minzeros=width*height
layer=[0 for _ in range(width*height)]
layers={}
for d,i in zip(data,range(1,len(data)+1)):
	layer[i%(width*height)]=int(d)
	zcount+=1 if d=='0' else 0
	if i%(width*height)==0 and i!=0:
		if zcount<minzeros:
			minzeros=zcount
			index = count
		zcount=0
		layers[count]=layer.copy()
		count+=1
for d in layers[index]:
	ones+=1 if d==1 else 0
	twos+=1 if d==2 else 0
for i in range(len(layers)):
	layer=layers[i] if i==0 else layer
	for x in range(len(layer)):
		layer[x]=layers[i][x] if layer[x]==2 else layer[x]
print('Answer 1: ',ones*twos)
for i in range(len(layer)):
	print('') if (i-1)%(width)==0 and i!=0 else None
	print('#',end='') if layer[i]==1 else None
	print(' ',end='') if layer[i]==0 else None
