import csv
from collections import defaultdict

def clean_braces(st):
	open_braces =0
	clean_st = ""
	for ch in st:
		if(ch == '('):
			open_braces+=1;
		if not open_braces:
			clean_st+=ch
		if ch == ')':
			open_braces-=1
			open_braces = max(0,open_braces)
	return clean_st
single_items = defaultdict(lambda: 0)
pair_items = defaultdict(lambda: 0)
transaction_count = 0;
with open("datasets/ingredients.csv") as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		transaction_count += 1
		raw_ingredients = clean_braces(row['features.value'].lower().replace("*newline*","").replace("*","").replace(".","").replace("and",","));
		ingre = []
		
		for item in raw_ingredients.split(','):
			item = item.strip()
			if item:
				ingre.append(item)
				single_items[item]+=1

		for i in range(len(ingre)):
			for j in range(i+1,len(ingre)):
				for tt in range(j+1,len(ingre)):
					key = ""
					for k in sorted([ingre[i],ingre[j],ingre[tt]]):
						key += (k +"_");
					pair_items[key]+=1
		if transaction_count%1000 == 0:
			print(transaction_count)

for support_value in reversed(range(2,50)):
	support_value *= transaction_count/100
	print("-----------------------------{:.2f}-----------------".format(support_value))
	# for (key,value) in single_items.items():
	# 	if (value > support_value):
	# 		print(key,value)

	for (key,value) in pair_items.items():
		if (value > support_value and value < support_value+100):
			print(key,value)