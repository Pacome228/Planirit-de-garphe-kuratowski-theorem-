import networkx as nx
########## K5 ###########
K5=nx.Graph()
K5_edges=[(1,2),(1,3),(1,4),(1,5),(2,3),(2,4),(2,5),(3,4),(3,5),(4,5)]
K5.add_edges_from(K5_edges)
########## K3_3 ###########
K3_3=nx.Graph()
K3_3_edges=[(1,4),(1,5),(1,6),(2,4),(2,5),(2,6),(3,4),(3,5),(3,6)]
K3_3.add_edges_from(K3_3_edges)
######### Graph with less than 5 edges #######
#First
K4=nx.Graph()
K4_edges=[(1,2),(1,3),(1,4),(2,3),(2,4),(3,4)]
K4.add_edges_from(K4_edges)
#Second
graph1=nx.Graph()
graph1_edges=[(1,2),(1,3),(2,3),(1,1)]
graph1.add_edges_from(graph1_edges)
#Third
graph2=nx.Graph()
graph2_edges=[(1,2),(1,3),(1,4),(2,3),(2,4),(3,4)]
graph2.add_edges_from(graph2_edges)
######### Complex graphs ########
graph3=nx.Graph()
graph3_edges=[(1,6),(1,4),(2,3),(2,7),(2,6),(3,7),(4,5),(5,7),(6,7)]
graph3.add_edges_from(graph3_edges)
graph3.add_node(8)
#PETERSEN GRAPH
petersen=nx.Graph()
petersen_edges=[(1,3),(1,4),(1,6),(2,4),(2,5),(2,7),(3,5),(3,8),(4,9),(5,10),(6,7),(6,10),(7,8),(8,9),(9,10)]
petersen.add_edges_from(petersen_edges)
petersen.add_node(8)