import pandas as pd
import os
import percentageCluster2 as pc
import math
import numpy as np
from ast import literal_eval

geo_dir = os.path.dirname('C:\Users\Dario\Desktop\  ')
file=open(geo_dir+'\set&perc.csv')
Reader=pd.read_csv(file)
file2=open(geo_dir+'\StintsPercentageWithout.csv')
Reader2=pd.read_csv(file2)
file3=open(geo_dir+'\Clipping_Analysis_crescini.csv')
Reader3=pd.read_csv(file3)
Reader3.stints=Reader3.stints.apply(literal_eval)
Stints=[]
test_stints=[]
test_alphas_bayesian=[]
test_alphas_time=[]
test_alphas_mileage=[]
Clusters=[]
Sets=[]
Tires=[]
street_types=['%of_service','%residential','%unclassified','%tertiary','%secondary','%primary','%trunk']
#Ys of the linear regression
mileage_alpha=[]
time_alpha=[]
bayesian_alpha=[]
X_matrix=[]
X_matrix_mileage=[]
Y_mileage=[]
Y_mileage_bayesian=[]
Y_time=[]
a_m=[]
a_b=[]
a_t=[]
#alphas for each street type
X_st=[]

for i,row in enumerate(Reader2['alpha']):
    if Reader2['model'][i]=='mileage':
        mileage_alpha.append(row)
    elif Reader2['model'][i]=='mileage_bayesian':
        bayesian_alpha.append(row)
    elif Reader2['model'][i]=='time':
        time_alpha.append(row)

for j,r in enumerate(Reader['Stint']):
    if r not in Stints:
        Stints.append(r)
    if Reader['Cluster'][j] not in Clusters:
        Clusters.append(Reader['Cluster'][j])

Clusters.sort()
Stints.sort()
stint_cluster_numbers=[]
for s in Stints:
    tot_number=Reader[(Reader.Stint==s)].count()['Stint']
    for c in Clusters:
        stint_cluster_numbers.append(float(Reader[(Reader.Stint==s)&(Reader.Cluster==c)].count()['Cluster'])/tot_number)
    X_matrix.append(stint_cluster_numbers)
    stint_cluster_numbers=[]

for st,row in enumerate(Reader2['%of_service']):
    X_st.append([float(Reader2['%of_service'][st])/100,
                 float(Reader2['%residential'][st])/100,
                 float(Reader2['%unclassified'][st])/100,
                 float(Reader2['%tertiary'][st])/100,
                 float(Reader2['%secondary'][st])/100,
                 float(Reader2['%primary'][st])/100,
                 float(Reader2['%trunk'][st])/100,
                 float(Reader2['%motorway'][st])/100,
                 #float(Reader2['%others'][st])/100
                 ])

X_st=[X_st[x-3] for x in range(3,len(X_st)+3,3)]

print X_st[-1]
X_st_m=list(X_st)
X_st_b=list(X_st)
X_st_t=list(X_st)


X_matrix_mileage=list(X_matrix)
X_matrix_mileage_bayesian=list(X_matrix)
X_matrix_time=list(X_matrix)
for i,row in enumerate(Reader2['model']):
    if row=='mileage':
        if math.isnan(Reader2['alpha'][i]):
            # if there are nan values it remove  the X_matrix elements correlated
            del X_matrix_mileage[Stints.index(int(Reader2['stints'][i].replace(']',"").replace('[',"")))]
            del X_st_m[Stints.index(int(Reader2['stints'][i].replace(']', "").replace('[', "")))]
        else:
            Y_mileage.append(Reader2['alpha'][i])
    elif row=='mileage_bayesian':
        if math.isnan(Reader2['alpha'][i]):
            # if there are nan values it remove  the X_matrix elements correlated
            del X_matrix_mileage_bayesian[Stints.index(int(Reader2['stints'][i].replace(']',"").replace('[',"")))]
            del X_st_b[Stints.index(int(Reader2['stints'][i].replace(']', "").replace('[', "")))]
        else:
            Y_mileage_bayesian.append(Reader2['alpha'][i])
    elif row=='time':
        if math.isnan(Reader2['alpha'][i]):
            # if there are nan values it remove  the X_matrix elements correlated
            del X_matrix_time[Stints.index(int(Reader2['stints'][i].replace(']',"").replace('[',"")))]
            del X_st_t[Stints.index(int(Reader2['stints'][i].replace(']', "").replace('[', "")))]
        else:
            Y_time.append(Reader2['alpha'][i])

for i,tire in enumerate(Reader3['TireID']):
    if (tire,Reader3['TirePosition'][i]) not in Tires:
        Tires.append((tire,Reader3['TirePosition'][i],Reader3['TruckID']))
for t in Tires:
    max = Reader3['stints_len'].where(Reader3.TireID==t[0]).where(Reader3.TirePosition==t[1]).where(Reader3.TruckID==t[2]).max()
    for lista in Reader3[Reader3['stints']==Reader3['stints'].where(Reader3.stints_len==max).where(Reader3.TireID==t[0]).where(Reader3.TirePosition==t[1])].stints:
        if lista[-1] not in test_stints:
            test_stints.append(lista[-1])
    #print Reader3.stints.where(Reader3.stints_len==int(max)).max()
    #test_stints.append(Reader3.stints.where(Reader3.stints_len==int(max)))
print test_stints




print 'k-fold cross validation mileage error: ',pc.k_fold(X_matrix_mileage,Y_mileage,9)
print 'k-fold cross validation time error:    ',pc.k_fold(X_matrix_time,Y_time,9)
print 'k-fold cross validation bayesian error:',pc.k_fold(X_matrix_mileage_bayesian,Y_mileage_bayesian,9)

#with intercept i need to remove an element, if i remove it from X_matrix it would be eliminated also in the other X_matrixs
for i,x in enumerate(X_matrix):
    del x[-1]



results_m=pc.regression(X_matrix_mileage,Y_mileage)
results_b=pc.regression(X_matrix_mileage_bayesian,Y_mileage_bayesian)
results_t=pc.regression(X_matrix_time,Y_time)


a_m=results_m.params
a_b=results_b.params
a_t=results_t.params


#f_test_m=results_m.f_test(np.identity(2))

print a_m
print a_b
print a_t
print results_m.summary()
print results_b.summary()
print results_t.summary()

clusters_temp=[]
alpha_temp=[0]*3
for ts in test_stints:
    '''
    for i,row in enumerate(Reader['Stint']):
        if row==ts:
            clusters_temp.append(Reader['Cluster'][i])


    for c in Clusters:
        alpha_temp[0] =alpha_temp[0]+clusters_temp.count(c)*a_m[c]/len(clusters_temp)
        alpha_temp[1] =alpha_temp[1]+ clusters_temp.count(c)*a_t[c]/len(clusters_temp)
        alpha_temp[2] =alpha_temp[2]+ clusters_temp.count(c)*a_b[c]/len(clusters_temp)
    '''
    for i,row in enumerate(Reader2['stints']):
        if int(row.replace(']',"").replace('[',""))==ts:
            clusters_temp.append([float(Reader2['%of_service'][st])/100,
                 float(Reader2['%residential'][st])/100,
                 float(Reader2['%unclassified'][st])/100,
                 float(Reader2['%tertiary'][st])/100,
                 float(Reader2['%secondary'][st])/100,
                 float(Reader2['%primary'][st])/100,
                 float(Reader2['%trunk'][st])/100,
                 float(Reader2['%motorway'][st])/100,
                 #float(Reader2['%others'][st])/100
                 ])
            for i in range(8):
                alpha_temp[0] = alpha_temp[0] + clusters_temp[i]* a_m[i]
                alpha_temp[1] = alpha_temp[1] + clusters_temp[i]* a_t[i]
                alpha_temp[2] = alpha_temp[2] + clusters_temp[i]* a_b[i]
            alpha_temp[0] = alpha_temp[0] + a_m[i+1]
            alpha_temp[1] = alpha_temp[1] + a_t[i+1]
            alpha_temp[2] = alpha_temp[2] + a_b[i+1]

    test_alphas_mileage.append(alpha_temp[0])
    test_alphas_time.append(alpha_temp[1])
    test_alphas_bayesian.append(alpha_temp[2])
    clusters_temp=[]
    alpha_temp=[0]*3

print len(test_stints),len([x[0] for x in Tires]),len(test_alphas_mileage)





results_st_m=pc.regression(X_st_m,Y_mileage)
results_st_b=pc.regression(X_st_b,Y_mileage_bayesian)
results_st_t=pc.regression(X_st_t,Y_time)
print results_st_m.params
print results_st_b.params
print results_st_t.params
print results_st_m.summary()
print results_st_b.summary()
print results_st_t.summary()


print 'k-fold cross validation mileage error: ',pc.k_fold(X_st_m,Y_mileage,9)
print 'k-fold cross validation time error:    ',pc.k_fold(X_st_t,Y_time,9)
print 'k-fold cross validation bayesian error:',pc.k_fold(X_st_b,Y_mileage_bayesian,9)

print results_st_m.cov_params()
test={'Stint':test_stints,
      'MileageAlpha':test_alphas_mileage,'TimeAlpha':test_alphas_time,'BayesianAlpha':test_alphas_bayesian}
test_df=pd.DataFrame(data=test)
test_df.to_csv(geo_dir+'\TestCresciniAlphas.csv')