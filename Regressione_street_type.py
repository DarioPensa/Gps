import pandas as pd
import os
import percentageCluster2 as pc
import math
import numpy as np
from ast import literal_eval

def x2calculator(x):
    x2=[]
    x2sub=[]
    for xi in x:
        for i,xii in enumerate(xi):
            x2sub.append(xii)
            for j,xiii in enumerate(xi):
                if j>=i: #x1*x2==x2*x1
                    x2sub.append(xii*xiii)
        x2.append(x2sub)
        x2sub=[]
    return x2
def model_selection(model,x,y):
    xs_errors=[]
    xs_variance=[]
    xs_e=[]
    xs_v=[]

    elements=[]
    for i,element in enumerate(x[0]):
        Xs = [[item[i]] for item in x]
        k_e,v_e,RMSEP_e,RMSEP_v=pc.k_fold(Xs,y,5,model,str(i))
        xs_errors.append(k_e)
        xs_variance.append(v_e)
    min_e=min(xs_errors)
    print min_e
    #it take the index of the min error
    elements.append(xs_errors.index(min_e))
    xs_e.append(xs_errors)
    xs_v.append(xs_variance)
    min_sub,min_elements=subtest(x,y,elements,model,xs_e,xs_v)
    if min_e<min_sub:
        print 'errore minimo=',min_e,'parametri: ',elements
        return min_e,elements
    else:
        print 'errore minimo=', min_sub, 'parametri: ', min_elements
        return min_sub,min_elements

def subtest(x_tot,y,elements,model,xs_e,xs_v):
    xs_e=xs_e
    xs_v=xs_v
    Xs=[]
    row=[]
    errors=[]
    variances=[]
    elements_vector=[]
    sub_elements=elements[:]
    min_sub=10
    min_sub=[]
    min_e=10
    index=-1
    for i,xi in enumerate(x_tot[0]):
        if i not in elements:
            sub_elements.append(i)

            for xi in x_tot:
                for e in sub_elements:
                    row.append(xi[e])
                Xs.append(row)
                row=[]
            parameters=','.join(str(e) for e in sub_elements)
            k_e, v_e,RMSEP_e,RMSEP_v = pc.k_fold(Xs, y, 5, model,parameters)
            errors.append(k_e)
            variances.append(v_e)
            elements_vector.append(sub_elements)
            Xs=[]
            sub_elements=elements[:]
            min_e=min(errors)
            index=errors.index(min_e)
    xs_e.append(errors)
    xs_v.append(variances)
    if len(sub_elements)!=len(x_tot[0])-1:
        print min_e
        min_sub,min_elements=subtest(x_tot,y,elements_vector[index],model,xs_e,xs_v)
    else:

        #error bar plotting
        pc.error_bar(len(x_tot[0]),xs_e,xs_v)

    if min_sub<min_e:
        return min_sub,min_elements
    else:
        return min_e,elements_vector[index]




geo_dir = os.path.dirname('C:\Users\Darius\Desktop\  ')
file2=open(geo_dir+'\Clipping_Analysis_rivetti_single.csv')
Reader2=pd.read_csv(file2)
#file3=open(geo_dir+'\Clipping_Analysis.csv')
#Reader3=pd.read_csv(file3)
#Reader3.stints=Reader3.stints.apply(literal_eval)

models=['mileage','time','bayesian']
Stints=[]
test_stints=[]
test_alphas_bayesian=[]
test_alphas_time=[]
test_alphas_mileage=[]
mileage_alpha=[]
time_alpha=[]
bayesian_alpha=[]
street_types=['%of_service','%residential','%unclassified','%tertiary','%secondary','%primary','%trunk','%motorway']
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

x2_mileage=x2calculator(X_st_m)
print len(x2_mileage[0])
x2_time=x2calculator(X_st_t)
print len(x2_time[0])
x2_bayesian=x2calculator(X_st_b)
print len(x2_bayesian[0])



for model in models:
    print len(models)
    print model
    if model=='mileage':
        print 'ok'
        m_e,m_p=model_selection(model,X_st_m,Y_mileage)
        m__e_2,m_p_2=model_selection(model+'x2',x2_mileage,Y_mileage)
    elif model=='time':
        t_e,t_p=model_selection(model, X_st_t, Y_time)
        t_e_2, t_p_2 = model_selection(model+'x2', x2_time, Y_time)
    elif model=='bayesian':
        b_e,b_p=model_selection(model, X_st_b, Y_mileage_bayesian)
        b_e_2, b_p_2 = model_selection(model+'x2', x2_bayesian, Y_mileage_bayesian)

d={'min_error_x':[m_e,t_e,b_e],'parameters_x_':[m_p,t_p,b_p],'min_error_x2':[m__e_2,t_e_2,b_e_2],'parameters_x':[m_p_2,t_p_2,b_p_2]}
df=pd.DataFrame(data=d, index=['mileage','time','bayesian'])
df.to_csv(geo_dir+'\model_selection')
'''
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




'''

