import numpy as np
from numpy import array
from scipy.cluster.vq import vq, kmeans, whiten
import os
import pandas as pd
import matplotlib.pyplot as plt
from pylab import plot,show

features = []

geo_dir = os.path.dirname('C:\Users\Dario\Desktop\  ')
sensorLog=open(geo_dir+'\TireForTruck\Merged5000013.csv')
Reader=pd.read_csv(sensorLog)

for index, row in enumerate(Reader['Lat']):
    features.append((row,Reader['Long'][index]))

print features
centroids,distortion=kmeans(features,4)
print centroids

# assign each sample to a cluster
idx= vq(features,centroids)

plot(features[idx==0,0],features[idx==0,1],'blue',
     features[idx==1,0],features[idx==1,1],'red','''
     features[idx==2,0],features[idx==2,1],'green',
     features[idx==3,0],features[idx==3,1],'orange',
     features[idx==4,0],features[idx==4,1],'brown'
     ''')
plot(centroids[:,0],centroids[:,1],'sg',markersize=8)
show()