import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys
import os





geo_dir = os.path.dirname('C:\Users\Dario\Desktop\  ')
file=open(geo_dir+'\GpsDataRivetti.csv')
Reader_d=pd.read_csv(file)
file2=open(geo_dir+'\GpsEDataRivetti.csv')
Reader_e=pd.read_csv(file2)
dati1=Reader_d[Reader_d['ID']!='error']
dati2=Reader_e[Reader_e['ID']!='error']
frames=[dati1,dati2]
result=pd.concat(frames)
result['n']=pd.to_numeric(result['n'])
sorted=result.sort(['n'])
boh=sorted.reset_index(drop=True)
filew=open(geo_dir+'\GpsDataRivettiOk.csv','wt')
boh.to_csv(filew)

'''
Reader_d.loc[Reader_d.n.isin(Reader_e.n),['ID','Lat','Long','TruckID','TruckCo2Warning',
                                                 'TruckCo2Value','GenerationDate','TimeStamp','TruckMileage',
                                                 'MarkDeleted','Speed','HDOP','FirmeWareVersion','Error','address',
                                                 'type','importance']]=Reader_e[['ID','Lat','Long','TruckID','TruckCo2Warning',
                                                 'TruckCo2Value','GenerationDate','TimeStamp','TruckMileage',
                                                 'MarkDeleted','Speed','HDOP','FirmeWareVersion','Error','address',
                                                 'type','importance']]


for i,row in enumerate(Reader_d['ID']):
    print i
    if row=='error':
        Reader_d['n','ID','Lat','Long','TruckID','TruckCo2Warning',
                                                 'TruckCo2Value','GenerationDate','TimeStamp','TruckMileage',
                                                 'MarkDeleted','Speed','HDOP','FirmeWareVersion','Error','address',
                                                 'type','importance'][i]=Reader_e[['n','ID','Lat','Long','TruckID','TruckCo2Warning',
                                                 'TruckCo2Value','GenerationDate','TimeStamp','TruckMileage',
                                                 'MarkDeleted','Speed','HDOP','FirmeWareVersion','Error','address',
                                                 'type','importance'][i]]
        print Reader_e[['ID','Lat','Long','TruckID','TruckCo2Warning',
                                                 'TruckCo2Value','GenerationDate','TimeStamp','TruckMileage',
                                                 'MarkDeleted','Speed','HDOP','FirmeWareVersion','Error','address',
                                                 'type','importance'][i]]

#print Reader_d[Reader_d['ID']=='error']




#withoutErrors=Reader[Reader['ID']!='error']

#filew=open(geo_dir+'\SensorL11.csv','wt')
#soloL11.to_csv(filew)
'''