from collections import defaultdict
from graphviz import Digraph

data = [["Bread", "Milk"],
["Bread", "Diaper", "Beer", "Eggs"], 
["Milk", "Diaper", "Beer", "Coke"], 
["Bread", "Milk", "Diaper", "Beer"], 
["Bread", "Milk", "Diaper", "Coke"]]


def pre_process(data,min_sup=0):
	count = defaultdict(lambda: 0)
	for row in data:
		for item in row:
			count[item]+=1
	items = []
	for key,value in count.items():
		if value >= min_sup:
			items.append((value,key))
	items = [item for item in reversed(sorted(items))]
	print(items)
	p_data = []
	for row in data:
		p_row = []
		for item in items:
			if item[1] in row:
				p_row.append(item[1])
		p_data.append(p_row)
	return items, p_data

class FPNode:    
    def __init__(self, previous= None,item="None"):
        self.item = item
        self.link = None
        self.next = {}
        self.previous = previous
        self.count = 0

class NodeIndex:
	def __init__(self):
		self.head = {}
		self.tail = {}

	def insert(self,key,value):
		if key not in self.head:
			self.head[key] = value	
		else:
			self.tail[key].link = value

		self.tail[key] = value;

	def get(self,key):
		return self.head[key]

	def __str__(self):
		op = "NodeIndex{ \n"
		for item in self.head.keys():
			ptr = self.get(item)
			counts = []
			while ptr is not None:
				counts.append(ptr.count)
				ptr = ptr.link
			op+="\t{} : {}\n".format(item,counts);
		return op + "}"
			

def dfs(ptr):
	print(ptr.item,ptr.count)
	for value in ptr.next.values():
		dfs(value)

class FPTree:

	def __init__(self):
		self.root = FPNode();
		self.single_items = {};
		self.index = NodeIndex()

	def insert(self,pattern):
		ptr = self.root
		for item in pattern:
			if item not in ptr.next:
				node = FPNode(ptr,item)
				ptr.next[item] = node
				self.index.insert(item,node)
			ptr.count+=1
			ptr = ptr.next[item]
		ptr.count+=1
	
	def get_conditional_fp_tree(self,suffix):
		

	def dot(self):
		node_id = 1
		nodes = [self.root]
		ind = {}
		arrows = []
		labels = []
		links = []
		while len(nodes):
			ptr = nodes[-1]
			nid = str(node_id)
			node_id+=1
			ind[ptr] = nid
			
			nodes.pop()
			nodes += ptr.next.values()
			if ptr.previous is not None:
				arrows.append((ind[ptr.previous],nid))
			if ptr.link is not None:
				links.append((ptr,ptr.link))

			labels.append((nid,"{}: {:2d}".format(ptr.item,ptr.count)))

		g = Digraph(comment='The Round Table')
		for item in labels:
			g.node(item[0],item[1])

		for edge in arrows:
			g.edge(edge[0],edge[1])

		for edge in links:
			g.edge(ind[edge[0]],ind[edge[1]],color="blue",style="dashed",constraint='false')
		print(g.source)
		g.render()




items,p_data = pre_process(data,2)

tree = FPTree()

for itemset in p_data:
	tree.insert(itemset)
print(p_data)
dfs(tree.root)
print(tree.index)

tree.dot()