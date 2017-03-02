import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys
import os

geo_dir = os.path.dirname('C:\Users\Dario\Desktop\  ')
SensorLog=open(geo_dir+'\GpsCresciniClean.csv')
SensorReader=pd.read_csv(SensorLog,dtype={'GeoPointID':int,'TireiD':int,'PressureTemp':int,'TruckID':int,'TireID':int,'WarningID':int},error_bad_lines=False, index_col=False)

SensorLog=open(geo_dir+'\GpsEDataCrescini.csv')
SensorReader=pd.read_csv(SensorLog,dtype={'GeoPointID':int,'TireiD':int,'PressureTemp':int,'TruckID':int,'TireID':int,'WarningID':int},error_bad_lines=False, index_col=False)


