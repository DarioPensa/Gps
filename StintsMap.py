import pandas as pd
from ast import literal_eval
import os
import numpy as np

alphas=[]
stints = []
geo_dir = os.path.dirname('C:\Users\Dario\Desktop\  ')
file=open(geo_dir+'\join.csv')
file2=open(geo_dir+'\StintsPercentageWithout.csv')
Reader=pd.read_csv(file)
Reader2=pd.read_csv(file2)
Reader=Reader.rename(columns={'type': 'desc'})

for row in Reader['Stint']:
    if row not in stints:
        stints.append(row)

table = pd.pivot_table(Reader2, values='alphas', index=['stints'],columns=['model'], aggfunc=np.sum)
print table
'''
for stint in stints:
        for i,row in enumerate(Reader2['stints']):
            if int(Reader2['stints'][i].replace(']',"").replace('[',"")) == stint:





#int(Reader2['stints'][i].replace(']',"").replace('[',"")) == stint:

for stint in stints:
    stint_file=Reader[Reader['Stint']==stint]
    stint_file.to_csv(geo_dir+'\stints\stint'+str(stint)+'.csv')


'''