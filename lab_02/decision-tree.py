import csv
from collections import defaultdict
from math import log2

data = []
att = []
decision_attr = 'play'
with open('tennis.csv') as csvfile:
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

	def __init__(self,attr):
		self.child = {}
		self.attr = attr

	def set(self,value,child):
		self.child[value] = child

def update_attributes(attributes,split):
	att = []
	for item in attributes:
		if item == split:
			continue
		att.append(item)
	return att

def make_decision_tree(data,attributes,decision):
	if len(attributes) == 1:
		return Dnode(attributes[0])
	
	attr_splits = {}
	e = get_entropy(data,decision)
	igs = []
	for split_attr in attributes:
		ex,splits = get_entropy_2(data,decision,split_attr)
		igs.append((e-ex,split_attr))
		attr_splits[split_attr] = splits
	igs.sort()
	split_attr = igs[-1][1]
	attributes = update_attributes(attributes,split_attr)
	root = Dnode(split_attr)
	for value,data in attr_splits[split_attr].items():
		root.set(value, make_decision_tree(data,attributes,decision))
	return root



# for item in attr:
# 	print(item,get_entropy_2(data,decision_attr,item))
# 	print("info gain",information_gain(data,decision_attr,item))
hello = make_decision_tree(data,attr,decision_attr)

def dfs(ptr):
	print(ptr.attr)
	for item in ptr.child.values():
		dfs(item)

dfs(hello)