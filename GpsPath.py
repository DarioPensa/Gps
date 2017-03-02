import scipy
from scipy.stats import pearsonr
import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys
import os

geo_dir = os.path.dirname('C:\Users\Dario\Desktop\  ')
sensorLog=open(geo_dir+'\TireForTruck\Merged5000007.csv')
Reader=pd.read_csv(sensorLog)

file3 =open(geo_dir+'\TireForTruck\Path5000007.csv','wt')
writer=csv.writer(file3, lineterminator='\n')
writer.writerow(['TimeStamp','TruckID','TirePosition','TireID','TruckMileage','State','Cap','type'])
for index, row in enumerate(Reader['ID_x']):
    writer.writerow([Reader['TimeStamp'][index],Reader['TruckID_x'][index],Reader['TirePosition'][index],Reader['TireID'][index],Reader['TruckMileage'][index],Reader['address'][index].split(',')[-1],Reader['address'][index].split(',')[-2],Reader['type'][index]])
