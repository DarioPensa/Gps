import pandas as pd
import os
import percentageCluster2 as pc
import math
import numpy as np
from ast import literal_eval

geo_dir = os.path.dirname('C:\Users\Dario\Desktop\  ')
file2=open(geo_dir+'\Clipping_Analysis_rivetti_single.csv')
Reader2=pd.read_csv(file2)
file3=open(geo_dir+'\Clipping_Analysis_rivetti.csv')
Reader3=pd.read_csv(file3)
Reader3.stints=Reader3.stints.apply(literal_eval)

Stints=[]
test_stints=[]
test_alphas_bayesian=[]
test_alphas_time=[]
test_alphas_mileage=[]
mileage_alpha=[]
time_alpha=[]
bayesian_alpha=[]
street_types=['%of_service','%residential','%unclassified','%tertiary','%secondary','%primary','%trunk']
X_st=[]
Y_mileage=[]
Y_mileage_bayesian=[]
Y_time=[]

for i,row in enumerate(Reader2['alpha']):
    if Reader2['model'][i]=='mileage':
        mileage_alpha.append(row)
    elif Reader2['model'][i]=='mileage_bayesian':
        bayesian_alpha.append(row)
    elif Reader2['model'][i]=='time':
        time_alpha.append(row)

for j,r in enumerate(Reader2['stints']):
    n= r.replace(']', "").replace('[', "")
    if int(n) not in Stints:
        Stints.append(int(n))

for st,row in enumerate(Reader2['%of_service']):
    X_st.append([float(Reader2['%of_service'][st])/100,
                 #float(Reader2['%residential'][st])/100,
                 float(Reader2['%unclassified'][st])/100,
                 float(Reader2['%tertiary'][st])/100,
                 float(Reader2['%secondary'][st])/100,
                 float(Reader2['%primary'][st])/100,
                 float(Reader2['%trunk'][st])/100,
                 float(Reader2['%motorway'][st])/100,
                 #float(Reader2['%others'][st])/100
                 ])
X_st=[X_st[x-3] for x in range(3,len(X_st)+3,3)]
X_st_m=list(X_st)
X_st_b=list(X_st)
X_st_t=list(X_st)

for i,row in enumerate(Reader2['model']):
    if row=='mileage':
        if math.isnan(Reader2['alpha'][i]):
            # if there are nan values it remove  the X_matrix elements correlated
            del X_st_m[Stints.index(int(Reader2['stints'][i].replace(']', "").replace('[', "")))]
        else:
            Y_mileage.append(Reader2['alpha'][i])
    elif row=='mileage_bayesian':
        if math.isnan(Reader2['alpha'][i]):
            # if there are nan values it remove  the X_matrix elements correlated
            del X_st_b[Stints.index(int(Reader2['stints'][i].replace(']', "").replace('[', "")))]
        else:
            Y_mileage_bayesian.append(Reader2['alpha'][i])
    elif row=='time':
        if math.isnan(Reader2['alpha'][i]):
            # if there are nan values it remove  the X_matrix elements correlated
            del X_st_t[Stints.index(int(Reader2['stints'][i].replace(']', "").replace('[', "")))]
        else:
            Y_time.append(Reader2['alpha'][i])

results_st_m=pc.regression(X_st_m,Y_mileage)
results_st_b=pc.regression(X_st_b,Y_mileage_bayesian)
results_st_t=pc.regression(X_st_t,Y_time)
a_st_m=results_st_m.params
a_st_b=results_st_b.params
a_st_t=results_st_t.params
print results_st_m.summary()
print results_st_t.summary()
print results_st_b.summary()

kfe_m,kfe_v_m=pc.k_fold(X_st_m,Y_mileage,9)
kfe_t,kfe_v_t=pc.k_fold(X_st_t,Y_time,9)
kfe_b,kfe_v_b=pc.k_fold(X_st_b,Y_mileage_bayesian,9)

print 'k-fold cross validation mileage error: ',kfe_m,' variance: ',kfe_v_m
print 'k-fold cross validation time error:    ',kfe_t,' variance: ',kfe_v_t
print 'k-fold cross validation bayesian error:',kfe_b,' variance: ',kfe_v_b