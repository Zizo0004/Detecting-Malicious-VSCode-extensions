# calculating the cosine similarity between extensions. hard part is to optimize the process given there are 60k+ exes
# Interstingly some extensions seem to have suspicous descriptions like 'free money' or pirating

import pandas as pd
import csv
# convert the csv to a pandas dataframe
set = pd.read_csv('vscode_extensions_verified.csv')
set = set.drop_duplicates(subset=['Extension Name'], keep='first') #


from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

