import math
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys
import os
import pylab
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.manifold import MDS
from scipy import sparse
from Clusters import Spectral,DBscan
from scipy.stats import entropy

geo_dir = os.path.dirname('C:\Users\Dario\Desktop\  ')
file=open(geo_dir+'\StintspercentageWithout.csv')
Reader=pd.read_csv(file)
#print Reader.mean()


def box_plot_for_clusters_percentage(alphas,clusters):
    service=[]
    residential=[]
    unclassified=[]
    tertiary=[]
    secondary=[]
    primary=[]
    trunk=[]
    motorway=[]
    others=[]
    cluster_array = []
    axes=[]




    if len(alphas)==len(clusters):
        print 'fino a qui tutto bene'

    for cluster in clusters:
        if cluster not in cluster_array:
            cluster_array.append(cluster)

    aggiunta = []
    percentuali = []
    for i, valore in enumerate(cluster_array):
        for j, c in enumerate(clusters):
            if c == valore:
                service.append(alphas['%of_service'][j])
                residential.append(alphas['%residential'][j])
                unclassified.append(alphas['%unclassified'][j])
                tertiary.append(alphas['%tertiary'][j])
                secondary.append(alphas['%secondary'][j])
                primary.append(alphas['%primary'][j])
                trunk.append(alphas['%trunk'][j])
                motorway.append(alphas['%motorway'][j])
                others.append(alphas['%others'][j])

        percentuali.append((service,residential,unclassified,tertiary,secondary,primary,trunk,motorway,others))
        #plt.xlabel('street_types')
        #plt.ylabel('percentage')

        #plt.subplots(4, sharex=True, sharey=True)
        # Create an axes instance
        if len(axes)==0:
            axes.append(plt.subplot(411))
            axes[-1].set_ylabel('percentage')
            axes[-1].set_xlabel('street_type')

        else:
            axes.append(plt.subplot(411+len(axes),sharex=axes[0], sharey=axes[0]))
            axes[-1].set_ylabel('percentage')
        # basic plot


        # Create the boxplot
        bp = axes[-1].boxplot((service,residential,unclassified,tertiary,secondary,primary,trunk,motorway,others))

        # plt.boxplot(cluster_array)

        #azzeramento ad ogni iterazione
        service = []
        residential = []
        unclassified = []
        tertiary = []
        secondary = []
        primary = []
        trunk = []
        motorway = []
        others = []
    axes[-1].set_xlabel('street_type')
    plt.show()
    plt.close()

def KLmatrix(percentage_file):
    for i,element in enumerate(percentage_file):
        percentage_file[i] = [float(x) / 100 if x!=0 else 0.001  for x in element]


    entropy_matrix=[]
    row=[]
    for i in percentage_file:
        for j in percentage_file:
            row.append(entropy(i,j))
        entropy_matrix.append(row)
        row=[]

    #it finds the max value in the entropy matrix
    max_vect = map(max, entropy_matrix)
    max_value=max(max_vect)

    #similarity matrix is a matrix with 0 to 1 values
    similarity_matrix = []
    row = []
    for i in entropy_matrix:
        for j in i:
            row.append(1-j/max_value)
        similarity_matrix.append(row)
        row = []

    return similarity_matrix

def PCA_analysis(percentagesalphas):
    print percentagesalphas
    pca=PCA(n_components=2)
    new=pca.fit_transform(percentagesalphas)
    plt.plot(new,'ro')
    plt.show()


def multidimensional_scaling(percentagesalphas):
    mds=MDS(n_components=2, metric=True, n_init=4, max_iter=300, verbose=0, eps=0.001, n_jobs=1, random_state=None, dissimilarity='euclidean')
    fit=mds.fit_transform(percentagesalphas)
    plt.plot(fit, 'ro')
    plt.show()

def testing(clusters,alphas,model):
    cluster_array=[]
    provone=[]
    percentualone=[]
    percentage_means=[]
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



    media=[0,0,0,0,0,0,0,0,0]
    for per in percentualone:
        for p in per:
            for i,element in enumerate(p):
                media[i]=media[i]+element
        percentage_means.append([x / len(per) for x in media])
        media=[0,0,0,0,0,0,0,0,0]
    print percentage_means
    plt.xlabel('Clusters')
    plt.ylabel(model)

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


def clustering(Reader):
    percentage_file = []
    file_for_pca = []  # it is the percentage file without 'others'
    clusters = []
    alphas = []
    clustering = []

    bayesian_file = []
    mileage_file = []
    time_file = []
#creation of the cosin similarity matrix
    for i,row in enumerate(Reader['%motorway']):
    # print Reader['%motorway'][i],Reader['%of_service'][i],Reader['%others'][i],Reader['%primary'][i],Reader['%residential'][i],Reader['%secondary'][i],Reader['%tertiary'][i],Reader['%trunk'][i],Reader['%unclassified'][i]
        if i%3==0:
            percentage_file.append([Reader['%motorway'][i],Reader['%of_service'][i],Reader['%others'][i],Reader['%primary'][i],Reader['%residential'][i],Reader['%secondary'][i],Reader['%tertiary'][i],Reader['%trunk'][i],Reader['%unclassified'][i]])


    #print percentage_file
    A =  np.array(percentage_file)
    A_sparse = sparse.csr_matrix(A)
    #similarities = cosine_similarity(A_sparse)
    #create a vector (cluster,alpha)
    similarities=KLmatrix(percentage_file)
    #cluster_labels= Spectral(similarities)
    print similarities
    cluster_labels=DBscan(similarities)
    stint_clustering=[x for x in cluster_labels for i in range(3)]
    print stint_clustering
    #da aggiungere lo stint



    #divides file in the three kind of trainer
    bayesian_file=Reader[Reader['model']=='mileage_bayesian'].reset_index()
    mileage_file=Reader[Reader['model']=='mileage'].reset_index()
    time_file=Reader[Reader['model']=='time'].reset_index()
    #boxplots of the percentage with respect to the clusters
    box_plot_for_clusters_percentage(bayesian_file,cluster_labels)

    for i in percentage_file:
        file_for_pca.append((i[0],i[1],i[3],i[4],i[5],i[6],i[7],i[8]))
    file_for_pca=StandardScaler().fit_transform(file_for_pca)
    PCA_analysis(file_for_pca)
    multidimensional_scaling(file_for_pca)


    #percentage_and_median(cluster_labels,bayesian_file['alpha'])
    testing(cluster_labels,bayesian_file,'bayesian_alpha')#prova tutto il vettore non solo alpha
    #plotting(cluster_labels,bayesian_file['alpha'])
    #percentage_and_median(cluster_labels,mileage_file['alpha'])
    testing(cluster_labels,mileage_file,'mileage_alpha')
    #plotting(cluster_labels,mileage_file['alpha'])
    #percentage_and_median(cluster_labels,time_file['alpha'])
    testing(cluster_labels,time_file,'time_alpha')
    #  plotting(cluster_labels,time_file['alpha'])
    return stint_clustering


'''
#also can output sparse matrices
similarities_sparse = cosine_similarity(A_sparse,dense_output=False)
print('pairwise sparse output:\n {}\n'.format(similarities_sparse))
'''