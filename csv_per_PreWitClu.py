import pandas as pd
from ast import literal_eval
import os
from datetime import datetime
import percentageCluster as pc

stints = []
stints_dates=[]
geo_dir = os.path.dirname('C:\Users\Dario\Desktop\  ')
file=open(geo_dir+'\join.csv')
file2=open(geo_dir+'\StintsPercentageWithout.csv')
Reader=pd.read_csv(file,parse_dates=['GenerationDate'])
Reader2=pd.read_csv(file2)

for row in Reader['Stint']:
    if row not in stints:
        stints.append(row)

new=[]
for s in stints[:2]:
    new.append(s)
    for i,row in enumerate(Reader['Stint'][:10000]):
        if row==s:
            new.append(Reader['GenerationDate'][i])
    stints_dates.append(new)
    new=[]


#stint,first timestamp,last timestamp, delta time
for i,row in enumerate(stints_dates):
    stints_dates[i]=row[0],row[1],row[-1],row[-1]-row[1]

print stints_dates[0]
pc.clustering(Reader2)

