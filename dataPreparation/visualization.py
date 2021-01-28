import networkx as nx
import netwulf as nw
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("GraphData3.csv")
print(df)

G=nx.from_pandas_edgelist(df, "node1", "node2")
#print([e for e in G.edges])




netw, _ = nw.visualize(G)
fig, ax = nw.draw_netwulf(netw)


# G = nx.Graph()
# G.add_nodes_from([0,1,2,'a','b','c'])
# G.add_edges_from([(0,1),('a','b')])
#
# network, config = nw.visualize(G,config={'zoom':3})
#
# # draw links only at first
# fig, ax = nw.draw_netwulf(network,draw_nodes=False)
#
# # get positions of two unconnected nodes to draw a link anyway
# v0 = nw.node_pos(network, 'c')
# v1 = nw.node_pos(network, 2)
# ax.plot([v0[0],v1[0]],[v0[1],v1[1]],c='#d95f02')
#
# # draw nodes now
# nw.draw_netwulf(network,fig,ax,draw_links=False)
#
# # add labels to a node and an edge
# nw.add_node_label(ax,network,'c')
# nw.add_edge_label(ax,network,('a','b'))