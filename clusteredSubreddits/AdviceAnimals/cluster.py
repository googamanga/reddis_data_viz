import pandas as pd
from collections import Counter
import json

count1 = 0
while count1 < 11:
	count1 = count1 + 1
	cnt = Counter()
	data = pd.read_csv("cluster" + str(count1) + ".csv")
	for sentence in data["nouns"]:
	  if isinstance(sentence, basestring):
	    print sentence
	    sentence = sentence.split()
	    for word in sentence:
	      print word
	      cnt[word] +=1
	print cnt
	columns = ['nouns', 'frequency']
	index = range(0, 10000)
	freq = pd.DataFrame(index=index, columns=columns)
	count = 0
	for word in cnt:
	  freq["nouns"][count] = word
	  freq["frequency"][count] = cnt[word]
	  count = count + 1
	freq = freq.sort_index(by='frequency', ascending=False) 
	f_new = open("JSON/cluster" + str(count) + ".json", 'w')
	d = [ 
	    dict([
	        (colname, row[i]) 
	        for i,colname in enumerate(freq.columns)
	    ])
	    for row in freq.values
	]
	f_new_stage = json.dumps(d)
	f_new.write(f_new_stage+'\n')