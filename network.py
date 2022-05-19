import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
from data_read import Read


class Network():
    def pandas_mat_2_stack(init,dataframe):
        stack = dataframe.stack()
        stack1 = stack[stack >= 1].rename_axis(('source', 'target')).reset_index(name='weight')
        stack2 = stack[stack == 0].rename_axis(('source', 'target')).reset_index(name='weight')
        all_stack = pd.concat([stack1,stack2])
        return all_stack

    def stack_2_graph(init,stack):
        graph = nx.from_pandas_edgelist(stack,edge_attr=True)
        return graph

    
    def plot_graph(init,Graph,stack):
        plt.figure(figsize = (100,70))
        nx.draw(Graph,
                with_labels=True,
                node_color = "red",
                node_size = [v * 5 for v in dict(Graph.degree()).values()],
                width = [v for v in stack["weight"].to_numpy()] 
                )
        ax = plt.gca()
        ax.collections[0].set_edgecolor("#687295")
        plt.show()
        
def main():
    net = Network()
    pr_pr = Read().mat_protein_protein()
    stack =net.pandas_mat_2_stack(pr_pr)
    graph = net.stack_2_graph(stack)
    net.plot_graph(graph,stack)


if __name__ == '__main__':
    main()    