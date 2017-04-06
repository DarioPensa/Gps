import csv
import pandas as pd
import igraph
from igraph import *
import os
import matplotlib.pyplot as plt
import scipy as sp


def get_spaced_colors(n):
    color_number= range(0,n)
    print n
    max_value = 16581375  # 255**3
    interval = int(max_value / (n*n))
    print interval
    colors = []
    for i in color_number:
        colors.append((interval/3*i,interval/3*i,interval/3*i))

    return colors

tutteLeVolte=[]
verticiEVolte=[]
graph=[]
Edges=[]
colori=[]
cap_graph= Graph()
geo_dir = os.path.dirname('C:\Users\Dario\Desktop\  ')
sensorLog=open(geo_dir+'\TireForTruck\Path5000007.csv')
Reader=pd.read_csv(sensorLog)
for index, row in enumerate(Reader['Cap']):
    tutteLeVolte.append(row[0:3])
    if row[0:3] not in graph:
        graph.append(row[0:3])
    if index!=len(Reader['Cap'])-1:
        if Reader['Cap'][index][0:3]!=Reader['Cap'][index+1][0:3]:
            Edges.append((row[0:3],Reader['Cap'][index+1][0:3]))

for element in graph:
    verticiEVolte.append((tutteLeVolte.count(element),element)) #(volte,elemento)


base= sorted(verticiEVolte,key=lambda student: student[0],reverse=True)[0][1]


cap_graph.add_vertices(graph)#i need different values
cap_graph.vs["name"]=graph
cap_graph.add_edges(Edges)
for i,value in enumerate(graph):
    if value==base:
        print'entrato'
        colori.append('#FF1F35')
    else:
        colori.append((str('#%02x%02x%02x'%(60+2*i,60+2*i,60+2*i))))
cap_graph.vs["color"]=colori

cap_graph.es["betweenness"]=cap_graph.count_multiple(Edges)
layout=cap_graph.layout("kamada_kawai")
cap_graph.vs["label"] = cap_graph.vs["name"]
igraph.plot(cap_graph,layout=layout)


cap_graph.write_svg('C:\Users\Dario\Desktop\TireForTruck\grafo.svg',labels='name',colors='color',width=650,height=650)