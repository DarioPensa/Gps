import scipy
from scipy.stats import pearsonr
import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys
import os


geo_dir = os.path.dirname('C:\Users\Dario\Desktop\  ')
file= open(geo_dir+'\GeoPointCrescini.csv')
fileWithErrors = open(geo_dir+'\GpsDataCrescini.csv','rb')

ReaderErrors=pd.read_csv(fileWithErrors)
Reader =pd.read_csv(file)



errors =[]
unClassified=[]

errors=Reader[Reader['ID']=='error']
unClassified=Reader[Reader['type']=='unclassified']




#errorsRows=Reader[ReaderErrors['ID']=='error']
#print (errorsRows)
#Result=open(geo_dir+'\cresciniErrorRows.csv','wt')
#errorsRows.to_csv(Result)


errorsProportion=float(len(errors))/float(len(Reader['ID']))
unClassifiedPercentage=float(len(unClassified))/float(len(Reader['ID']))*100

print('errors percentage =',errorsProportion*100)
print ('unclassified percentage=',unClassifiedPercentage)









#def dataCleaner(GPSFile):


