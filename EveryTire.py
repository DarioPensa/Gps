import scipy
from scipy.stats import pearsonr
import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys
import os

geo_dir = os.path.dirname('C:\Users\Dario\Desktop\  ')
sensorLog=open(geo_dir+'\GpsRivetti\SensorLog.csv')
Reader=pd.read_csv(sensorLog)

TruckIDs = []

TireIDs = []
Rows=[]


for index, row in enumerate(Reader['TruckID']):

    if row not in TruckIDs:
        TruckIDs.append(row)
        Rows.append(index)
for index, row in enumerate(Reader['TireID']):
    if index in Rows and row not in TireIDs:
        TireIDs.append(row)

print TireIDs


for tire in TireIDs:
    Writer = open(geo_dir + '\GpsRivetti\Tire'+str(tire)+'.csv', 'wt')
    singleTireCsv=Reader[Reader['TireID']==tire]
    singleTireCsv.to_csv(Writer)
