import math
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys
import os
import pylab
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.decomposition import PCA
from scipy import sparse
from Clusters import Spectral,DBscan

geo_dir = os.path.dirname('C:\Users\Dario\Desktop\  ')
file=open(geo_dir+'\StintspercentageWithout.csv')
Reader=pd.read_csv(file)
#print Reader.mean()
percentage_file=[]
clusters=[]
alphas=[]
clustering=[]

bayesian_file=[]
mileage_file=[]
time_file=[]

def PCA_analysis(percentagesalphas):
    PCA.fit(percentagesalphas)


def testing(clusters,alphas):
    cluster_array=[]
    provone=[]
    percentualone=[]

    provone.append([])
    for cluster in clusters:
        if cluster not in cluster_array:
            cluster_array.append(cluster)
    aggiunta = []
    percentuali=[]
    for i,valore in enumerate(cluster_array):
        for j,c in enumerate(clusters):
            if c==valore:
                percentuali.append((alphas['%of_service'][j],alphas['%residential'][j],alphas['%unclassified'][j],alphas['%tertiary'][j],alphas['%secondary'][j],alphas['%primary'][j],alphas['%trunk'][j],alphas['%motorway'][j],alphas['%others'][j]))
                aggiunta.append(alphas['alpha'][j])
        provone.append(aggiunta)
        percentualone.append(percentuali)
        aggiunta = []
        percentuali=[]
    for i in percentualone:
        print i
    # Create a figure instance
    fig = plt.figure(1, figsize=(9, 6))

    # Create an axes instance
    ax = fig.add_subplot(111)
    # basic plot


    # Create the boxplot
    bp = ax.boxplot(provone)

    #plt.boxplot(cluster_array)
    plt.show()


def percentage_and_median(cluster,alpha_file):
    cluster_alpha0 = []
    cluster_alpha1 = []
    cluster_alpha2 = []
    cluster_alpha3 = []
    for i, row in enumerate(cluster):
        if math.isnan(alpha_file[i]) == False:
            if row == 0:
                cluster_alpha0.append(alpha_file[i])
            elif row == 1:
                cluster_alpha1.append(alpha_file[i])
            elif row == 2:
                cluster_alpha2.append(alpha_file[i])
            elif row == 3:
                cluster_alpha3.append(alpha_file[i])
    print 'total mean ',alpha_file.mean()
    print reduce(lambda x, y: x + y, cluster_alpha0) / len(cluster_alpha0), np.median(cluster_alpha0)
    print reduce(lambda x, y: x + y, cluster_alpha1) / len(cluster_alpha1), np.median(cluster_alpha1)
    print reduce(lambda x, y: x + y, cluster_alpha2) / len(cluster_alpha2), np.median(cluster_alpha2)
    print reduce(lambda x, y: x + y, cluster_alpha3) / len(cluster_alpha3), np.median(cluster_alpha3)

def plotting(clusters,alphas):

    plt.plot(clusters, alphas, 'ro')
    plt.margins(0.1)
    plt.show()

#creation of the cosin similarity matrix
for i,row in enumerate(Reader['%motorway']):
   # print Reader['%motorway'][i],Reader['%of_service'][i],Reader['%others'][i],Reader['%primary'][i],Reader['%residential'][i],Reader['%secondary'][i],Reader['%tertiary'][i],Reader['%trunk'][i],Reader['%unclassified'][i]
    if i%3==0:
        percentage_file.append([Reader['%motorway'][i],Reader['%of_service'][i],Reader['%others'][i],Reader['%primary'][i],Reader['%residential'][i],Reader['%secondary'][i],Reader['%tertiary'][i],Reader['%trunk'][i],Reader['%unclassified'][i]])

#print percentage_file
A =  np.array(percentage_file)
A_sparse = sparse.csr_matrix(A)
similarities = cosine_similarity(A_sparse)
#create a vector (cluster,alpha)
cluster_labels= Spectral(similarities)
prova=DBscan(similarities)
#divides file in the three kind of trainer
bayesian_file=Reader[Reader['model']=='mileage_bayesian'].reset_index()
mileage_file=Reader[Reader['model']=='mileage'].reset_index()
time_file=Reader[Reader['model']=='time'].reset_index()



percentage_and_median(cluster_labels,bayesian_file['alpha'])
testing(cluster_labels,bayesian_file)#prova tutto il vettore non solo alpha
#plotting(cluster_labels,bayesian_file['alpha'])
percentage_and_median(cluster_labels,mileage_file['alpha'])
testing(cluster_labels,mileage_file)
#plotting(cluster_labels,mileage_file['alpha'])
percentage_and_median(cluster_labels,time_file['alpha'])
testing(cluster_labels,time_file)
#plotting(cluster_labels,time_file['alpha'])



'''
#also can output sparse matrices
similarities_sparse = cosine_similarity(A_sparse,dense_output=False)
print('pairwise sparse output:\n {}\n'.format(similarities_sparse))
'''

