##########################  PLANARITY TESTING MODULE ################################
                        ####  AUTHOR:DANDJI Ayawo Désiré & Fenitra Ramiaramanana ####
import networkx as nx
import matplotlib.pyplot as plt
import itertools as it
from networkx.algorithms import bipartite




def is_simple_graph(graph):
    """
        Return true if the graph is simple and false in the other case
    """
    if(nx.is_empty(graph)):
        return True
    return True if nx.number_of_selfloops(graph)==0 else False




def create_copy(graph):
    new_graph = nx.Graph()
    new_graph.add_nodes_from(graph)
    new_graph.add_edges_from(graph.edges)
    return new_graph




def is_K_5(graph):
    """
        Return true if the graph is a complete graph with 5 nodes
    """
    return True if (len(nx.edges(graph))==10 and len(nx.nodes(graph))==5) else False



def is_subdivision_of_K_5():
    return "IS_SUBDIVISION_OF_K5"




def is_K_3_3(graph):
    """
        Return true if the graph is a complete biparte graph with 6 nodes
        and each set contains 3 nodes
    """
    if(not (bipartite.is_bipartite(graph))):
        return False
    if(not len(nx.nodes(graph))==6):
        return False
    if(not len(nx.edges(graph))==9):
        return False
    set1,set2=bipartite.sets(graph)
    return True if len(set1)==3 else False




def is_subdivision_of_K_3_3():
    return "IS_SUBDIVISION_OF_K3_3"




def simple_cases_of_planarity(graphe):
    #Is a K5
    if(is_K_5(graphe)):
        return False,is_subdivision_of_K_5(),graphe,graphe
    #Is a K3_3
    if(is_K_3_3(graphe)):
        return False,is_subdivision_of_K_3_3(),graph,graphe
    #if graph has less or equal than 4 nodes,it's planar
    
    number_of_nodes=len(nx.nodes(graphe))

    #Graph has at most 6 nodes and is neither K5 nor K3_3
    if(number_of_nodes<=6):
        return True
   
    



def graph_cleaning(graph):
    nodes_degree_zero=[node for node in nx.nodes(graph) if nx.degree(graph,node)==0]
    graph.remove_nodes_from(nodes_degree_zero)
def get_planarity_parameters(graph):
    nb_nodes_at_least_degree_3=0
    nb_nodes_at_least_degree_4=0
    for node in nx.nodes(graph):
        if(nx.degree(graph,node)>=3):
            nb_nodes_at_least_degree_3+=1
        if(nx.degree(graph,node)>=4):
            nb_nodes_at_least_degree_4+=1
    return nb_nodes_at_least_degree_3,nb_nodes_at_least_degree_4




def get_nodes_with_degree_2(graph):
    nodes_with_degree_2=[]
    for node in nx.nodes(graph):
        if(nx.degree(graph,node)==2):
                nodes_with_degree_2.append(node)
    return nodes_with_degree_2




def reducing(graph):
    nodes_with_degree_2=get_nodes_with_degree_2(graph)
    for node in nodes_with_degree_2:
        neighbors=list(nx.neighbors(graph,node))
        if len(neighbors)==2:
            graph.add_edge(neighbors[0],neighbors[1])
            graph.remove_node(node)
    return graph




def bad_subdivision(graph,n_l_d_3,n_l_d_4):
    nodes=graph.nodes()
    for i in range(5,len(nodes)+1):
        for subnodes in it.combinations(nodes,i):
            subgraph=graph.subgraph(subnodes)
            copy_of_subgraph=create_copy(subgraph)
            reduction_of_subgraph=reducing(copy_of_subgraph)
            if(n_l_d_4>=5):
                #We look for subgraph in our graph wich is subdivision of K5
                    if(is_K_5(reduction_of_subgraph)):
                        return False,is_subdivision_of_K_5(),subgraph,reduction_of_subgraph
            if(n_l_d_3 >=6):
                #We look for subgraph in our graph wich is subdivision of K3_3
                if(is_K_3_3(reduction_of_subgraph)):
                        return False,is_subdivision_of_K_3_3(),subgraph,reduction_of_subgraph 

    


def is_planar(graph):
    """
    Return True if graph is Planar of False with counter-example if graph is non planar
    We use Kuratowski's approach by looking for a subdivision of K5 or K3_3 in our graph
    If we found such subdivion, then the graph is non planar
    """
    
    result=simple_cases_of_planarity(graph)
    if(result is not None):
        return (result,None) if ((result is True)) else result
    else:
        #Since nodes with degree 0 does not affect planarity, we remove them
        #We also look for number of nodes of degree at least 3 or at least 4
        graph_cleaning(graph)
        n_l_d_3,n_l_d_4=get_planarity_parameters(graph)
        if (n_l_d_3 <6) and (n_l_d_4<5):
            return True,None
        if(n_l_d_3 >=6) or (n_l_d_4>=5):
            result=bad_subdivision(graph,n_l_d_3,n_l_d_4)
            if(result is not None):
                return result         
        return True,None

