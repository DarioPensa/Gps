import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys
import os

stints = []
geo_dir = os.path.dirname('C:\Users\Dario\Desktop\  ')
file=open(geo_dir+'\join.csv')
file2=open(geo_dir+'\StintsPercentageWithout.csv')
Reader=pd.read_csv(file)
Reader2=pd.read_csv(file2)


for row in Reader['Stint']:
    if row not in stints:
        stints.append(row)

for stint in stints:
    stint_file=Reader[Reader['Stint']==row]
    stint_file.to_csv(geo_dir+'\stints\stint'+str(stint)+'.csv')


