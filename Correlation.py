import scipy
from scipy.stats import pearsonr
import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys
import os
import pylab

speed=[]
type=[]
streetTypes=['service','residential','unclassified','tertiary','secondary','primary','trunk','motorway']#,'parking']
def typeToNumber(argument):
    switcher = {
        'service':0,
        'residential':1,
        'unclassified':2,
        'tertiary':3,
        'secondary':4,
        'primary':5,
        'trunk':6,
        'motorway':7,
        #'parking':9
    }
    return switcher.get(argument,8)



geo_dir = os.path.dirname('C:\Users\Dario\Desktop\merged\  ')
mergedGps=open(geo_dir+'\Merged5000013.csv')
Reader=pd.read_csv(mergedGps)


for row in Reader['Speed']:
    speed.append(row)
for row in Reader['type']:
    type.append(typeToNumber(row))

#noFermi=Reader[Reader['Speed']!=0]
plt.plot(type,speed,'ro')
plt.show()
#plt.plot(noFermi['Speed'],noFermi['Temperature'],'ro')

plt.plot(type,Reader['Temperature'],'ro')
plt.show()
plt.close()
print('correlation temperature,speed =',pearsonr(Reader['Temperature'],Reader['Speed']))
print('correlation speed,street type =',pearsonr(speed,type))

for row in Reader['type']:
     typeToNumber(row)==0
        #print row

for index,street in enumerate(streetTypes):
    print'the percentage of street type :',street,' is equal to',int(float(type.count(index))/float(len(type))*100),'%'
    print 'number of data of type',street, 'is', type.count(index)



pylab.show()


