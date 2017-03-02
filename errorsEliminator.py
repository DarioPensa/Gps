import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys
import os

TirePosition = 'L-1-1'
addressList=[]
truck1=[]
truck2=[]
truck3=[]
truck4=[]
truck5=[]
truck6=[]
truck7=[]
truck8=[]

truck1when=[]
truck2when=[]
truck3when=[]
truck4when=[]
truck5when=[]
truck6when=[]
truck7when=[]
truck8when=[]


geo_dir = os.path.dirname('C:\Users\Dario\Desktop\  ')
file=open(geo_dir+'\provaTotCrescini.csv')
Reader=pd.read_csv(file,error_bad_lines=False, index_col=False)
for index, row in enumerate(Reader['ID']):
    addressList.append((Reader['TruckID'][index],Reader['address'][index].split(','),Reader['TimeStamp'][index]))

for row in addressList:
    if row[0]==5000001 and row[1][-1] not in truck1:
        truck1.append(row[1][-1])
        truck1when.append(row[2])

    if row[0]==5000002 and row[1][-1] not in truck2:
        truck2.append(row[1][-1])
        truck2when.append(row[2])
    if row[0]==5000003 and row[1][-1] not in truck3:
        truck3.append(row[1][-1])
        truck3when.append(row[2])
    if row[0]==5000004 and row[1][-1] not in truck4:
        truck4.append(row[1][-1])
        truck4when.append(row[2])
    if row[0]==5000005 and row[1][-1] not in truck5:
        truck5.append(row[1][-1])
        truck5when.append(row[2])
    if row[0]==5000006 and row[1][-1] not in truck6:
        truck6.append(row[1][-1])
        truck6when.append(row[2])
    if row[0]==5000007 and row[1][-1] not in truck7:
        truck7.append(row[1][-1])
        truck7when.append(row[2])
    if row[0]==5000008 and row[1][-1] not in truck8:
        truck8.append(row[1][-1])
        truck8when.append(row[2])

print'stati visitati dal truck 5000001 :'
for index, row in enumerate(truck1):
    print truck1[index],truck1when[index]

print'stati visitati dal truck 5000002 :'
for index, row in enumerate(truck2):
    print truck2[index],truck2when[index]

print'stati visitati dal truck 5000003 :'
for index, row in enumerate(truck3):
    print truck3[index],truck3when[index]
print'stati visitati dal truck 5000004 :'
for index, row in enumerate(truck4):
    print truck4[index],truck4when[index]
print'stati visitati dal truck 5000005 :'
for index, row in enumerate(truck5):
    print truck5[index],truck5when[index]
print'stati visitati dal truck 5000006 :'
for index, row in enumerate(truck6):
    print truck6[index],truck6when[index]
print'stati visitati dal truck 5000007 :'
for index, row in enumerate(truck7):
    print truck7[index],truck7when[index]
print'stati visitati dal truck 5000008 :'
for index, row in enumerate(truck8):
    print truck8[index],truck8when[index]




#withoutErrors=Reader[Reader['ID']!='error']

#filew=open(geo_dir+'\SensorL11.csv','wt')
#soloL11.to_csv(filew)
