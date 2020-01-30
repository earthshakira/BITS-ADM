import csv
from collections import defaultdict
from math import log2
from graphviz import Digraph
data = []
att = []
decision_attr = 'play'
with open('c_tennis.csv') as csvfile:
	reader = csv.DictReader(csvfile)
	att = reader.fieldnames
	for row in reader:
		data.append(row)

attr = []

for item in att:
	if item != decision_attr:
		attr.append(item)

print(attr)

def  get_entropy(data,attr):
	frequency_table = defaultdict(lambda:0)
	n = 0;
	for item in data:
		frequency_table[item[attr]]+=1
		n += 1
	entropy = 0;

	for item in frequency_table.values():
		p = item/n;
		entropy += -1 * p * log2(p);
	return entropy


def pure_split(data,attr):
	splits = defaultdict(lambda:[])
	for item in data:
		d = {}
		for key,value in item.items():
			if key == attr:
				continue
			d[key] = value
		splits[item[attr]].append(d)
	return splits

def get_entropy_2(data,attr,split_attr):
	print("d",attr,split_attr)
	splits = pure_split(data,split_attr)
	n = len(data)
	entropy = 0;
	for (key,split) in splits.items():
		entropy += len(split)/n * get_entropy(split,attr);
	return entropy,splits

class Dnode:
	ids = 0
	def __init__(self,attr,ig):
		self.id = str(Dnode.ids)
		Dnode.ids+=1;
		print(self.id)
		self.child = {}
		self.ig = ig;
		self.attr = attr

	def set(self,value,child):
		self.child[value] = child

	def dot(self,g=None):
		if g is None:
			g = Digraph(comment='FP Tree')
		print()
		if self.ig == 0:
			g.attr('node', shape='box')
			g.node(self.id,label="{}".format(self.attr))
			g.attr('node', shape='ellipse')
		else:
			g.node(self.id,label="{} {:.04f}".format(self.attr,self.ig))
		for attr,child in self.child.items():
			child.dot(g)
			g.edge(self.id,child.id,label=attr)
		return g

def update_attributes(attributes,split):
	att = []
	for item in attributes:
		if item == split:
			continue
		att.append(item)
	return att

def make_decision_tree(data,attributes,decision):
	if len(attributes) == 1:
		return Dnode(attributes[0],get_entropy(data,decision))
	
	attr_splits = {}
	e = get_entropy(data,decision)
	igs = []
	for split_attr in attributes:
		ex,splits = get_entropy_2(data,decision,split_attr)
		igs.append((e-ex,split_attr))
		attr_splits[split_attr] = splits
	igs.sort()
	split_attr = igs[-1][1]
	if igs[-1][0] == 0.0:
		d = defaultdict(lambda:0)
		for c in data:
			d[c[decision]]+=1;
		p = 0
		ans = None
		n = len(data)
		for key,f in d.items():
			if f/n > p:
				p = f/n;
				ans = key
		return Dnode("{}({:.4f})".format(ans,p),0)
	attributes = update_attributes(attributes,split_attr)
	root = Dnode(split_attr,igs[-1][0])
	for value,data in attr_splits[split_attr].items():
		root.set(value, make_decision_tree(data,attributes,decision))
	return root



# for item in attr:
# 	print(item,get_entropy_2(data,decision_attr,item))
# 	print("info gain",information_gain(data,decision_attr,item))
tree = make_decision_tree(data,attr,decision_attr)

tree.dot().view()

