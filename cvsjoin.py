import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys
import os

TirePosition = 'L-1-1'

geo_dir = os.path.dirname('C:\Users\Dario\Desktop\  ')

SensorLog=open(geo_dir+'\GpsRivetti\Tire5000009.csv')
SensorReader=pd.read_csv(SensorLog,dtype={'GeoPointID':int,'TireiD':int,'PressureTemp':int,'TruckID':int,'TireID':int,'WarningID':int},error_bad_lines=False, index_col=False)




GpsData=open(geo_dir+'\GpsDataRivetti.csv')
GpsReader=pd.read_csv(GpsData)
GpsReader=GpsReader[GpsReader['ID']!='error']
GpsReader['TruckID']=np.dtype(int)
#print(GpsReader)

Result=open(geo_dir+'\GpsRivetti\Merged\Tire5000009Merged.csv','wt')
join=pd.merge(SensorReader,GpsReader,how='inner',left_on='GeoPointID',right_on='ID')
join.to_csv(Result)

#new=pd.DataFrame.join(SensorReader ,GpsReader,on='GeoPointID',how='inner')



#joined=open(geo_dir+'\joinedGps'+TruckID+TirePosition+'.csv','wt')