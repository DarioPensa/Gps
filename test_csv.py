import os
import percentageCluster2 as pc
import pandas as pd
from ast import literal_eval
import math

def x2calculator(x):
    x2=[]
    x2sub=[]
    for xi in x:
        for i,xii in enumerate(xi):
            x2sub.append(xii)
            for j,xiii in enumerate(xi):
                if j>=i: #x1*x2==x2*x1
                    x2sub.append(float("{0:.4f}".format(xii*xiii)))
        x2.append(x2sub)
        x2sub=[]
    return x2

Tires=[]
test_stints=[]
test_alphas_bayesian=[]
test_alphas_time=[]
test_alphas_mileage=[]
test_alphas_bayesian2=[]
test_alphas_time2=[]
test_alphas_mileage2=[]
geo_dir = os.path.dirname('C:\Users\Dario\Desktop\  ')
file1=open(geo_dir + '\model_selection_crescini.csv')
Reader1=pd.read_csv(file1)
Reader1.parameters_x=Reader1.parameters_x.apply(literal_eval)
Reader1.parameters_x2=Reader1.parameters_x2.apply(literal_eval)
file2 = open(geo_dir + '\Clipping_Analysis.csv')
Reader2 = pd.read_csv(file2)
file3 = open(geo_dir + '\Clipping_Analysis.csv')
Reader3 = pd.read_csv(file3)
Reader3.stints = Reader3.stints.apply(literal_eval)

x_m_ind=[int(xmi) for xmi in Reader1.parameters_x[0]]
x_m2_ind=[int(xm2i)for xm2i in Reader1.parameters_x2[0]]
x_t_ind=[int(xti)for xti in Reader1.parameters_x[1]]
x_t2_ind=[int(xt2i)for xt2i in Reader1.parameters_x2[1]]
x_b_ind=[int(xbi)for xbi in Reader1.parameters_x[2]]
x_b2_ind=[int(xb2i)for xb2i in Reader1.parameters_x2[2]]
Stints = []
test_stints = []
mileage_alpha = []
time_alpha = []
bayesian_alpha = []
X_st = []
Y_mileage = []
Y_mileage_bayesian = []
Y_time = []

for i, row in enumerate(Reader2['alpha']):
    if Reader2['model'][i] == 'mileage':
        mileage_alpha.append(row)
    elif Reader2['model'][i] == 'mileage_bayesian':
        bayesian_alpha.append(row)
    elif Reader2['model'][i] == 'time':
        time_alpha.append(row)

for j, r in enumerate(Reader2['stints']):
    n = r.replace(']', "").replace('[', "")
    if int(n) not in Stints:
        Stints.append(int(n))

for st, row in enumerate(Reader2['%of_service']):
    X_st.append([float(Reader2['%of_service'][st]) / 100,
                    float(Reader2['%residential'][st]) / 100,
                     float(Reader2['%unclassified'][st]) / 100,
                     float(Reader2['%tertiary'][st]) / 100,
                     float(Reader2['%secondary'][st]) / 100,
                     float(Reader2['%primary'][st]) / 100,
                     float(Reader2['%trunk'][st]) / 100,
                     float(Reader2['%motorway'][st]) / 100,
                     # float(Reader2['%others'][st])/100
                     ])
X_st = [X_st[x - 3] for x in range(3, len(X_st) + 3, 3)]
X_st_m = list(X_st)
X_st_b = list(X_st)
X_st_t = list(X_st)

for i, row in enumerate(Reader2['model']):
    if row == 'mileage':
        if math.isnan(Reader2['alpha'][i]):
                # if there are nan values it remove  the X_matrix elements correlated
            del X_st_m[Stints.index(int(Reader2['stints'][i].replace(']', "").replace('[', "")))]
        else:
            Y_mileage.append(Reader2['alpha'][i])
    elif row == 'mileage_bayesian':
        if math.isnan(Reader2['alpha'][i]):
            # if there are nan values it remove  the X_matrix elements correlated
            del X_st_b[Stints.index(int(Reader2['stints'][i].replace(']', "").replace('[', "")))]
        else:
            Y_mileage_bayesian.append(Reader2['alpha'][i])
    elif row == 'time':
        if math.isnan(Reader2['alpha'][i]):
            # if there are nan values it remove  the X_matrix elements correlated
            del X_st_t[Stints.index(int(Reader2['stints'][i].replace(']', "").replace('[', "")))]
        else:
            Y_time.append(Reader2['alpha'][i])

x2_mileage = x2calculator(X_st_m)
x2_time = x2calculator(X_st_t)
x2_bayesian = x2calculator(X_st_b)

for i, tire in enumerate(Reader3['TireID']):
    if (tire, Reader3['TirePosition'][i]) not in Tires:
        Tires.append((tire, Reader3['TirePosition'][i], Reader3['TruckID']))
for t in Tires:
    max = Reader3['stints_len'].where(Reader3.TireID == t[0]).where(Reader3.TirePosition == t[1]).where(
        Reader3.TruckID == t[2]).max()
    for lista in Reader3[Reader3['stints'] == Reader3['stints'].where(Reader3.stints_len == max).where(
                    Reader3.TireID == t[0]).where(Reader3.TirePosition == t[1])].stints:
        if lista[-1] not in test_stints:
            test_stints.append(lista[-1])
                # print Reader3.stints.where(Reader3.stints_len==int(max)).max()
                # test_stints.append(Reader3.stints.where(Reader3.stints_len==int(max)))
print test_stints

#x_m_ind=Reader1.parameters_x[0]
#x_m2_ind=Reader1.parameters_x2[0]
#x_t_ind=Reader1.parameters_x[1]
#x_t2_ind=Reader1.parameters_x2[1]
#x_b_ind=Reader1.parameters_x[2]
#x_b2_ind=Reader1.parameters_x2[2]
Xm=[]
Xt=[]
Xb=[]
X2m=[]
X2t=[]
X2b=[]

for xm in X_st_m:
    Xm.append([xm[int(ind)] for ind in x_m_ind])
for x2m in x2_mileage:
    X2m.append([x2m[int(ind1)] for ind1 in x_m2_ind])
for xt in X_st_t:
    Xt.append([xt[int(ind2)] for ind2 in x_t_ind])
for x2t in x2_time:
    X2t.append([x2t[int(ind3)] for ind3 in x_t2_ind])
for xb in X_st_b:
    Xb.append([xb[int(ind4)] for ind4 in x_b_ind])
for x2b in x2_bayesian:
    X2b.append([x2b[int(ind5)] for ind5 in x_b2_ind])


clusters_temp=[]
alpha_temp=[0]*6

results_st_m=pc.regression(Xm,Y_mileage)
results_st_m2=pc.regression(X2m,Y_mileage)
results_st_b=pc.regression(Xb,Y_mileage_bayesian)
results_st_b2=pc.regression(X2b,Y_mileage_bayesian)
results_st_t=pc.regression(Xt,Y_time)
results_st_t2=pc.regression(X2t,Y_time)


a_st_m=results_st_m.params
a_st_m2=results_st_m2.params
a_st_b=results_st_b.params
a_st_b2=results_st_b2.params
a_st_t=results_st_t.params
a_st_t2=results_st_t2.params

#print results_st_m.cov_params()
latest_stint=-1
for ts in test_stints:

    for i, row in enumerate(Reader2['stints']):
        if int(row.replace(']', "").replace('[', "")) == ts and latest_stint != ts:
            latest_stint = ts
            clusters_temp = [float(Reader2['%of_service'][i]) / 100,
                             float(Reader2['%residential'][i]) / 100,
                             float(Reader2['%unclassified'][i]) / 100,
                             float(Reader2['%tertiary'][i]) / 100,
                             float(Reader2['%secondary'][i]) / 100,
                                 float(Reader2['%primary'][i]) / 100,
                                 float(Reader2['%trunk'][i]) / 100,
                                 float(Reader2['%motorway'][i]) / 100,
                                 # float(Reader2['%others'][i])/100
                                 ]
            clusters_temp2=x2calculator([clusters_temp])
            Xtest_m=[clusters_temp[i]for i in x_m_ind]
            X2test_m=[clusters_temp2[0][i] for i in x_m2_ind]
            Xtest_t=[clusters_temp[i]for i in x_t_ind]
            X2test_t=[clusters_temp2[0][i]for i in x_t2_ind ]
            Xtest_b=[clusters_temp[i]for i in x_b_ind]
            X2test_b=[clusters_temp2[0][i]for i in x_b2_ind]

            for i,j in enumerate(Xtest_m):
                alpha_temp[0]=alpha_temp[0]+j*a_st_m[i]
            alpha_temp[0]=alpha_temp[0]+a_st_m[i+1]
            for i,j in enumerate(X2test_m):
                alpha_temp[1] = alpha_temp[1] + j * a_st_m2[i]
            alpha_temp[1] = alpha_temp[1] + a_st_m2[i + 1]

            for i,j in enumerate(Xtest_t):
                alpha_temp[2]=alpha_temp[2]+j*a_st_t[i]
            alpha_temp[2]=alpha_temp[2]+a_st_t[i+1]
            for i,j in enumerate(X2test_t):
                alpha_temp[3] = alpha_temp[3] + j * a_st_t2[i]
            alpha_temp[3] = alpha_temp[3] + a_st_t2[i + 1]

            for i,j in enumerate(Xtest_b):
                alpha_temp[4]=alpha_temp[4]+j*a_st_b[i]
            alpha_temp[4]=alpha_temp[4]+a_st_b[i+1]
            for i,j in enumerate(X2test_b):
                alpha_temp[5] = alpha_temp[5] + j * a_st_b2[i]
            alpha_temp[5] = alpha_temp[5] + a_st_b2[i + 1]


            test_alphas_mileage.append(alpha_temp[0])
            test_alphas_mileage2.append(alpha_temp[1])
            test_alphas_time.append(alpha_temp[2])
            test_alphas_time2.append(alpha_temp[3])
            test_alphas_bayesian.append(alpha_temp[4])
            test_alphas_bayesian2.append(alpha_temp[5])

    clusters_temp = []
    alpha_temp = [0] * 6

# print len(test_stints),len([x[0] for x in Tires]),len(test_alphas_mileage),len(test_alphas_bayesian),len(test_alphas_time)

test = {'Stint': test_stints,
        'MileageAlpha': test_alphas_mileage,'MileageAlpha2': test_alphas_mileage2,'TimeAlpha': test_alphas_time,
        'TimeAlpha2': test_alphas_time2,'BayesianAlpha':test_alphas_bayesian,'BayesianAlpha2':test_alphas_bayesian2}



test_df = pd.DataFrame(data=test)
test_df.to_csv(geo_dir + '\Test_crescini\Testcrescini.csv')