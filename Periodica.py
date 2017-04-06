import os
import pandas as pd
import Clusters as cl
import numpy as np

LOC=[]#A movement sequence
spots=[]#"places",binary sequence  ith= 1 if the object is in b at timestamp i
DFT=[] #discrete Fourier transform

geo_dir = os.path.dirname('C:\Users\Dario\Desktop\  ')
sensorLog=open(geo_dir+'\TireForTruck\Merged5000047.csv')
Reader=pd.read_csv(sensorLog)
features = []
#spots finding and binary in-out
for index, row in enumerate(Reader['Lat']):
    features.append((row,Reader['Long'][index]))

cl.Affinity(features)
centroids,closest_centroid=cl.K_means(features)
for i,element in enumerate(centroids):
    spots.append([0]*len(Reader['Lat']))

for i, element in enumerate(closest_centroid):
    for j,spot in enumerate(spots):

        if element==j:
            spots[j][i]=1

#detect periods in each spot

print(np.fft.fft(spots))






print len(closest_centroid)




#for elements in centroids:


#stage 1 detect periods
#1.1 find reference spots



