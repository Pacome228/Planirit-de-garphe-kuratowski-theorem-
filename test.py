#!/usr/bin/python3
import planarity 
import networkx as nx
from networkx.algorithms import bipartite
import matplotlib.pyplot as plt
from graph_test import K5,K3_3,K4,petersen,petersen,petersen,petersen
import time


if planarity.is_simple_graph(petersen):
    t1=time.perf_counter()
    response=planarity.is_planar(petersen)
    #response=planarity.is_planar(K5)     #response[0] should return False
    #response=planarity.is_planar(K4)     #response[0] should return True
    #response=planarity.is_planar(petersen) #response[0] should return True
    #response=planarity.is_planar(graphe2)#response[0] should return True
    #response=planarity.is_planar(graphe3)#response[0] should return True
    t2=time.perf_counter()
    print(response[0])
    print("Response time {}".format(t2-t1))
    if(not response[0]):
        if(response[1]==planarity.is_subdivision_of_K_5()):
            print("This graph contains a subdivision of K5")        
            nx.draw(response[2], with_labels=True, arrows = False, connectionstyle='arc3, rad = 0.1')
            plt.savefig('subgraph_with_subdivision.png')
            plt.figure()
            nx.draw(response[3], with_labels=True, arrows = False, connectionstyle='arc3, rad = 0.1')
            plt.savefig('subgraph_without_subdivision.png')
        if(response[1]==planarity.is_subdivision_of_K_3_3()):
            print("This graph contains a subdivision of K_3_3")        
            nx.draw(response[2], with_labels=True, arrows = False, connectionstyle='arc3, rad = 0.1')
            plt.savefig('subgraph_with_subdivision.png')
            plt.figure()
            nx.draw_networkx(response[3],nx.drawing.layout.bipartite_layout(response[3], bipartite.sets(response[3])[0]),5)
            plt.savefig('subgraph_without_subdivision.png')




    ####### ALTERNATIVE TEST ##########
    try:
        nx.draw_planar(petersen,with_labels = True, alpha=0.8) 
        plt.savefig("planar_graph.png")
        print("Yes,This graph is planar")
    except:
        print("Sorry,this graph is not planar")
else:
    print("Le graphe n'est pas simple")