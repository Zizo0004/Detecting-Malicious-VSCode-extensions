# will neevd to optimize it later, no time so need to be quick
def Dam_Levenstein(str1, str2):
    d = {}
    max_dist = len(str1) + len(str2)
    for i in range(-1, len(str1) + 1):
        d[i, -1] = i + 1
    for j in range(-1, len(str2) + 1):
        d[-1, j] = j + 1        
    for i in range(len(str1)):
        for j in range(len(str2)):
            if str1[i] == str2[j]:
                cost = 0
            else:
                cost = 1
            d[i, j] = min(d[i-1, j] + 1,d[i, j-1] + 1,d[i-1, j-1] + cost)
            
            if i > 0 and j > 0 and str1[i] == str2[j-1] and str1[i-1] == str2[j]:
                d[i, j] = min(d[i, j], d[i-2, j-2] + cost)
    
    return d[len(str1)-1, len(str2)-1]

import pandas as pd
import csv
import time

df = pd.read_csv('vscode_extensions_verified.csv')
df = df.sort_index()

for i in df.iloc[1:10].iterrows():
        Dam_Levenstein(i[1]['Extension Name'], 'vscode-python')

