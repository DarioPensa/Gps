import scipy
from scipy.stats import pearsonr
import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys
import os
import pylab
from sklearn.metrics.pairwise import cosine_similarity
from scipy import sparse
from Clusters import Spectral

geo_dir = os.path.dirname('C:\Users\Dario\Desktop\  ')
file=open(geo_dir+'\StintspercentageWithout.csv')
file2=open(geo_dir+'\StintspercentageWith.csv')
Reader=pd.read_csv(file)
Reader2=pd.read_csv(file2)

for i,row in enumerate(Reader['alpha']):
    if Reader['alpha'][i]!=Reader2['alpha'][i]:
        print Reader['alpha'][i],Reader2['alpha'][i]

