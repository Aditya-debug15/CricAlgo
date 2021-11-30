from collections import defaultdict
import matplotlib.pyplot as plt
import networkx as nx 
tuples_for_edges_bo_ba_ru = []
tuples_for_edges_bo_ba_ru.append(("P SHAW","S DHAWAN",16))
tuples_for_edges_bo_ba_ru.append(("S DHAWAN","S IYER",3))
tuples_for_edges_bo_ba_ru.append(("S DHAWAN","R PANT",26))
tuples_for_edges_bo_ba_ru.append(("P SHAW","S IYER",8))
tuples_for_edges_bo_ba_ru.append(("P SHAW","R PANT",7))
tuples_for_edges_bo_ba_ru.append(("R PANT","S IYER",10))
G = nx.DiGraph()
plt.figure(figsize=(25,25))  

for tup in tuples_for_edges_bo_ba_ru:
    bo,ba,ru = tup       
    G.add_weighted_edges_from([(bo,ba,ru)])

edge_colors = [] 
for e  in G.edges():
    n1,n2 = e
    if G[n1][n2]["weight"] > 25:         
        edge_colors.append('red')
    elif G[n1][n2]["weight"] > 14:
        edge_colors.append('orange')
    else:
        edge_colors.append('blue')    
    
pos = []
pos = nx.circular_layout(G)  # positions for all nodes

nx.draw_networkx_nodes(G, pos, node_size=380)
nx.draw_networkx_edges(G, pos, width=2,arrowsize=22,edge_color=edge_colors)

## Adding the labels and changing font, font size.
weight_labels = nx.get_edge_attributes(G,'weight') 
nx.draw_networkx_edge_labels(G,pos,edge_labels=weight_labels,font_size=22, font_family="sans-serif") 

## Positioning the labels appropriately.
label_pos = pos
for k in pos.keys():
    label_pos[k]=pos[k]+[0,0.05]
nx.draw_networkx_labels(G, label_pos, font_size=25, font_family="sans-serif",font_color = 'purple')
plt.savefig('filename.png')
pr = nx.pagerank(G, alpha=0.9)
pr = sorted(pr.items(), key=lambda x: x[1],reverse = True)
for val in pr:
    print(val)