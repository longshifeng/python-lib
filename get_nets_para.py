import community
from networkx import Graph, average_clustering
import networkx as nx
import numpy as np
# I:/2019.7/2016.1-12_deal.edges/test.edges
def get_para(file_path):
    g=nx.read_edgelist(file_path)
    print("load finished")

    node_num=nx.number_of_nodes(g)
    # print(len(g.nodes()))#node_num
    # print(g.nodes())
    # print(len(g.edges()))#edge_num
    # print(average_clustering(g))#聚集系数

    # Find modularity
    part = community.best_partition(g)
    mod = community.modularity(part,g)#模块度

    path_length=nx.average_shortest_path_length(g)#路径长

    glo_efficiency=nx.algorithms.global_efficiency(g)

    result=str(node_num)+'\t'\
           # +str(len(g.edges()))+'\t'+str(average_clustering(g))+'\t'+str(mod)+'\t'+str(path_length)+'\t'+str(glo_efficiency)+'\n'
    return result

def cal_globaleffiency():
    import numpy as np
    np.seterr(divide='ignore')

    # Example using a random graph with 20 nodes
    g = Graph.Erdos_Renyi(20, 0.5)

    # Assign weights on the edges. Here 1s everywhere
    g.es["weight"] = np.ones(g.ecount())

    def nodal_eff(g):
        weights = g.es["weight"][:]
        sp = (1.0 / np.array(g.shortest_paths_dijkstra(weights=weights)))
        np.fill_diagonal(sp, 0)
        N = sp.shape[0]
        ne = (1.0 / (N - 1)) * np.apply_along_axis(sum, 0, sp)

        return ne

    eff = nodal_eff(g)
    print(eff)
    # [0.68421053 0.81578947 0.73684211 0.76315789 0.76315789 0.71052632
    # 0.81578947 0.81578947 0.81578947 0.73684211 0.71052632 0.68421053
    # 0.71052632 0.81578947 0.84210526 0.76315789 0.68421053 0.68421053
    # 0.78947368 0.76315789]
    aver_eff=np.mean(eff)

import os
dir_path='I:/2019.7/2016.1-12_deal.edges/'
# file=open(dir_path+"result.csv","w+")#处理路径下所有网络文件
# for root, dirs, files in os.walk(dir_path):
#     files.sort(reverse=False)  # files是路径下包含所有文件的遍历列表(乱序)
#     for filename in files:
#         if '20160101.as-rel.txt_deal.edges' in filename:
#             print(filename)
#             result=get_para(dir_path + filename)
# print(result+"\n")
result=get_para(dir_path + "20160101.as-rel.txt_deal.edges")
print(result+"\n")
