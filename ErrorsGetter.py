import csv
import sys
import os
import urllib, json
import pandas as pd

latitude=2
longitude=3
errorIndexes=[]
geo_dir = os.path.dirname('C:\Users\Dario\Desktop\  ')
file = open(geo_dir+'\GpsDataRivetti.csv')
Reader = csv.reader(file)
#Reader = Reader[Reader['ID']!='error']
file2= open(geo_dir+'\GeoPoint.csv')
Reader2=csv.reader(file2)
file3 =open(geo_dir+'\RivettiErroriGPS.csv','wt')
writer=csv.writer(file3, lineterminator='\n')


for index, row in enumerate(Reader):
    if row[1]=='error':
        errorIndexes.append(index)

for index,row in enumerate(Reader2):
    if index==0:
        writer.writerow(row)
    if index in errorIndexes:
        writer.writerow(row)









#for row in Reader2:
 #   writer.writerow((row[0],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14],row[15]))

