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
#Reader=Reader.rename(columns={'type': 'desc'})

desc=[]
new_alpha_column=[]
alphas=[]
alphaperstint=[]
for row in Reader['Stint']:
    if row not in stints:
        stints.append(row)

#table = pd.pivot_table(Reader2, values='alphas', index=['stints'],columns=['model'], aggfunc=np.sum)
#print table

for stint in stints:
        for i,row in enumerate(Reader2['stints']):
            if int(Reader2['stints'][i].replace(']',"").replace('[',"")) == stint:
                if stint not in alphaperstint:
                    alphaperstint.append(stint)
                alphaperstint.append(Reader2['alpha'][i])
        alphas.append(alphaperstint)
        alphaperstint=[]

for i,element in enumerate(Reader['Stint']):
    for al in alphas:
        if al[0]==element:
            new_alpha_column.append((al[1],al[2],al[3]))

#print new_alpha_column
Reader.insert(32,'alphas',new_alpha_column)
#print len(Reader['Stint'])
#for i,row in enumerate(Reader['Stint']):
#    desc.append((Reader['type'][i],Reader['alphas'][i]))
Reader["desc"] = Reader["type"].map(str) + Reader["alphas"].map(str)
#print len(desc)
#Reader.insert(33,'desc',desc)



print Reader['desc']




#int(Reader2['stints'][i].replace(']',"").replace('[',"")) == stint:

for stint in stints:
    stint_file=Reader[Reader['Stint']==stint]
    stint_file.to_csv(geo_dir+'\stints2\stint'+str(stint)+'.csv')


