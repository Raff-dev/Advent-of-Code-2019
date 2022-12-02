class tree():
	def __init__(self,name):
		self.parent=None
		self.name=name
		self.children=dict()
		trees[name]=self
	def add_child(self,child):
		self.children[child]=child.name
		child.parent=trees[self.name]
	def get_parent(self):
		if self.parent!=None:
			return self.parent.get_name()
	def get_name(self):
		return self.name

def count(tree,c):
	return count(trees[tree.get_parent()],c+1) if tree.get_parent()!=None else c

def find_parents(tree,parent_list=[]):
	if tree.get_parent()!=None:
		parent_list.append(tree.get_parent())
		return find_parents(trees[tree.get_parent()],parent_list) 
	return parent_list

data=open("day6_data.txt").read().split('\n')
trees=dict()
for pair in data:
	pair=pair.split(')')
	if pair[0] not in trees:
		tree(pair[0])
	trees[pair[0]].add_child(tree(pair[1]))
	
orbits=0
for tree in trees:
	orbits+=count(trees[tree],0)

my_parents=find_parents(trees['YOU'],[])
san_parents=find_parents(trees['SAN'],[])
common=set(my_parents)&set(san_parents)
if set(my_parents)<=set(san_parents):
	dist=len(set(san_parents)-common)
	print('abc')
elif set(san_parents)<=set(my_parents):
	dist=len(set(my_parents)-common)
	print('cba')
else:
	dist=len(my_parents)+len(san_parents)-2*len(common)
print('the total number of direct and indirect orbits:',orbits)
print('Minimum number of orbital transfers',dist)

