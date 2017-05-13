import pandas as pd
from ast import literal_eval
import os
from datetime import datetime
import percentageCluster as pc
import time

stints = []
stints_dates=[]
geo_dir = os.path.dirname('C:\Users\Dario\Desktop\  ')
file=open(geo_dir+'\join.csv')
file2=open(geo_dir+'\StintsPercentageWithout.csv')
Reader=pd.read_csv(file,parse_dates=['GenerationDate'])
Reader2=pd.read_csv(file2)

#get the clustering
clustering=pc.clustering(Reader2)
Reader2.insert(24,'Cluster',clustering)
for row in Reader['Stint']:
    if row not in stints:
        stints.append(row)

new=[]
for s in stints:
    new.append(s)
    for i,row in enumerate(Reader['Stint']):
        if row==s:
            new.append(Reader['GenerationDate'][i])
    stints_dates.append(new)
    new=[]

for j,date in enumerate(stints_dates):
    a=date[1:]
    for i,element in enumerate(date):
        if i==0:
            date[i]=element
        else:
            date[i]=a[i-1]
    stints_dates[j]= date
#stint,first timestamp,last timestamp, delta time
for i,row in enumerate(stints_dates):
    stints_dates[i]=row[0],row[1],row[-1],row[-1]-row[1]

first_timestamps=[x[1] for x in stints_dates]
last_timestamps=[x[2] for x in stints_dates]
delta_time=[x[3]for x in stints_dates]

first_timestamps=[x for x in first_timestamps for i in range(3)]
last_timestamps=[x for x in last_timestamps for i in range(3)]
delta_time=[x for x in delta_time for i in range(3)]

Reader2.insert(25,'InitialTimeStamp',first_timestamps)
Reader2.insert(26,'FinalTimeStamp',last_timestamps)
Reader2.insert(27,'DeltaTime',delta_time)

print stints_dates[0]
Reader2.to_csv(geo_dir+'\Wclusters.csv')
