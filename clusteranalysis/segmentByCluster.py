import pandas as pd

data = pd.read_csv("clusteredNouns.csv")


count = 1
while count < 11:
# 	if isinstance(subreddit, basestring):
# 	subset = data[[x.startswith(count) for x in data["kmeans"]]]
  subset = data[data["kmeans"] == count]
  subset.to_csv("cluster" + str(count) +".csv")
  count +=1

print data