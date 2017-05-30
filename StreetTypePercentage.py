import pandas as pd
from ast import literal_eval
import os
import csv_per_PreWitClu as cpp

sets=[]
Stints=[]
df = pd.DataFrame()

service=[]
residential=[]
tertiary=[]
secondary=[]
primary=[]
trunk=[]
motorway=[]
unclassified=[]
others=[]

geo_dir = os.path.dirname('C:\Users\Dario\Desktop\  ')
file=open(geo_dir+'\dtime_division.csv')
Reader=pd.read_csv(file,parse_dates=['GenerationDate'])

for i,set in enumerate(Reader['TimeDivisionSet']):
    if set not in sets:
        sets.append(set)
        Stints.append(Reader['Stint'][i])

for s in sets:
    single_set=Reader[Reader['TimeDivisionSet']==s]
    percentages=cpp.street_type_percentage(single_set)

    service.append(percentages[0])
    residential.append(percentages[1])
    tertiary.append(percentages[2])
    secondary.append(percentages[3])
    primary.append(percentages[4])
    trunk.append(percentages[5])
    motorway.append(percentages[6])
    unclassified.append(percentages[7])
    others.append(percentages[8])


df.insert(0,'set',sets)
df.insert(1,'Stint',Stints)
df.insert(2,'%of_service',service)
df.insert(3,'%residential',residential)
df.insert(4,'%tertiary',tertiary)
df.insert(5,'%secondary',secondary)
df.insert(6,'%primary',primary)
df.insert(7,'%trunk',trunk)
df.insert(8,'%motorway',motorway)
df.insert(9,'%unclassified',unclassified)
df.insert(10,'%others',others)



clustering=cpp.clustering(df)

df.insert(2,'Cluster',clustering)
df.to_csv(geo_dir+'\set&perc.csv')