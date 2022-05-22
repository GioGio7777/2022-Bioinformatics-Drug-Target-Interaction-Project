import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
from data_read import Read


class Network():
    def pandas_mat_2_stack(init, dataframe):
        stack = dataframe.stack()
        stack1 = stack[stack >= 1].rename_axis(
            ('source', 'target')).reset_index(name='weight')

        return stack1

    def stack_2_graph(init, stack):
        graph = nx.from_pandas_edgelist(
            stack, source="source", target="target", edge_attr=True, create_using=nx.DiGraph)
        return graph

    def plot_graph(init, Graph):
        fig, ax = plt.subplots(figsize=(100, 50))
        pos = nx.spring_layout(Graph)
        nx.draw_networkx_nodes(Graph, pos,
                               cmap=plt.get_cmap("viridis"),
                               node_size=4000)
        nx.draw_networkx_labels(Graph, pos)
        nx.draw_networkx_edges(Graph, pos, edge_color="r", arrows=True)

        plt.show()


def main():
    net = Network()
    pr_pr = Read().mat_protein_protein()
    stack = net.pandas_mat_2_stack(pr_pr)
    graph = net.stack_2_graph(stack)
    net.plot_graph(graph)


if __name__ == '__main__':
    main()
