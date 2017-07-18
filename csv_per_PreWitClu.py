import pandas as pd
from ast import literal_eval
import os
from datetime import datetime
import percentageCluster2 as pc
import time
import numpy as np

def clustering(df):
    return pc.clustering(df)


def typeToNumber(tipo):
    switcher = {
        'service': 0,
        'residential': 1,
        'tertiary': 2,
        'secondary': 3,
        'primary': 4,
        'trunk': 5,
        'motorway': 6,
        'unclassified': 7,
        # 'parking':9
    }
    return switcher.get(tipo, 8)


def street_type_percentage(df):
    type = []
    percentages = []
    streetTypes = ['service', 'residential', 'tertiary', 'secondary', 'primary', 'trunk', 'motorway', 'unclassified',
                   'otherTypes']


    for row in df['type']:
        type.append(typeToNumber(row))
    for index, street in enumerate(streetTypes):
        percentages.append(round(float(type.count(index)) / float(len(type)) * 100,2))
    return percentages
def main():
    stints = []
    stints_dates=[]
    test_stints=[]
    geo_dir = os.path.dirname('C:\Users\Dario\Desktop\  ')
    file=open(geo_dir+'\join.csv')
    file2=open(geo_dir+'\StintsPercentageWithout.csv')
    Reader=pd.read_csv(file,parse_dates=['GenerationDate'])
    Reader2=pd.read_csv(file2)
    stint_separati=[]

    division=[]
    sets=[]



#get the clustering
#clustering=pc.clustering(Reader2)
#Reader2.insert(24,'Cluster',clustering)
    for row in Reader['Stint']:
        if row not in stints:
            stints.append(row)


    Reader_sorted= Reader.sort_values(by=['Stint','GenerationDate'],ascending=[True,True]).reset_index()

    for i,row in enumerate(Reader_sorted['GenerationDate']):
        if not division:
            division.append(1)
            date_divise=row
        else:
            if np.timedelta64((np.datetime64(row) - np.datetime64(date_divise)), 'D')>=np.timedelta64(1, 'D') or Reader_sorted['Stint'][i]!=Reader_sorted['Stint'][i-1] :
                division.append(division[-1] + 1)
                date_divise=row

            else:
                division.append(division[-1])

    Reader_sorted.insert(31,'TimeDivisionSet',division)

    Reader_sorted.to_csv(geo_dir+'\dtime_division.csv')

    for i,set in enumerate(Reader_sorted['TimeDivisionSet']):
        if set not in sets:
            sets.append(set)
    print len(sets)
    for s in sets:
        single_set=Reader_sorted[Reader_sorted['TimeDivisionSet']==s]
        print street_type_percentage(single_set)






'''
for s in stints:
    stint_separati.append(Reader.loc[(Reader.Stint==s)])

print stint_separati

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
'''