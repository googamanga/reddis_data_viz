import pandas as pd

data = pd.read_csv("/Users/williamshelton/Desktop/reddis_data_viz/data/prototype.csv")

here = data["subreddit"]

unique = here.drop_duplicates()

unique.to_csv("/Users/williamshelton/Desktop/reddis_data_viz/data/unique_subreddit.csv")
