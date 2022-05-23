import streamlit as st
from data_read import Read
from network import Network
from node_2_vec import NodeVec
import networkx as nx
import matplotlib.pyplot as plt


class Streamlit:
    @st.cache()
    def table_protein(init):
        read = Read()
        return read.mat_protein_protein()

    @st.cache()
    def table_pr_dr(init):
        read = Read()
        return read.mat_protein_drug()

    @st.cache()
    def table_pr_di(init):
        read = Read()
        return read.mat_protein_disease()

    @st.cache()
    def table_dr_dr(init):
        read = Read()
        return read.mat_drug_drug()

    @st.cache()
    def table_dr_pr(init):
        read = Read()
        return read.mat_drug_protein()

    @st.cache()
    def table_dr_se(init):
        read = Read()
        return read.mat_drug_se()

    @st.cache()
    def table_dr_di(init):
        read = Read()
        return read.mat_drug_disease()

    def plot_graph(init, table):
        network = Network()
        stack = network.pandas_mat_2_stack(table)
        graph = network.stack_2_graph(stack)

        fig, ax = plt.subplots(figsize=(100, 50))
        pos = nx.spring_layout(graph)
        nx.draw_networkx_nodes(graph, pos,
                               cmap=plt.get_cmap("viridis"),
                               node_size=7000)
        nx.draw_networkx_labels(graph, pos)
        nx.draw_networkx_edges(graph, pos, edge_color="r", arrows=True)

        return fig

    def printElements(init, output, item, item2=""):
        elements = []
        for a in output:
            if a[0][0:1] != item and a[0][0:1] != item2:
                elements.append(a)
        return elements

    def printElements2(init, output, item):
        elements = []
        for a in output:
            if a[0][0:2] != item:
                elements.append(a)
        return elements

    def streamlit(init):
        network = Network()
        st.title("Introduction to Bioinformatics Project")

        menus = ["Protein-Protein Interaction",
                 "Protein-Drug Interaction",
                 "Protein-Disease Interaction",
                 "Drug-Disease Interaction",
                 "Drug-Drug Interaction",
                 "Drug-Side Effect Interaction",
                 "Drug-Protein Interaction"]

        choice = st.sidebar.selectbox("Menu", menus)

        if choice == "Protein-Protein Interaction":

            st.header("Protein-Protein Interaction")
            tablepr = init.table_protein()
            with st.container():
                if st.button("Show Graph"):
                    st.subheader("Graph Of Table")
                    with st.spinner(text='In progress'):
                        fig_prpr = init.plot_graph(tablepr)
                        st.pyplot(fig_prpr)
                        st.success("Graph is done")

            model_prpr = NodeVec().get_model("pr_pr.model")

            st.subheader("Interaction output")
            try:
                protein_name = st.text_input("Enter protein")

                if len(protein_name) != 0:
                    values_prpr = NodeVec().returnSimilars(model_prpr, protein_name)
                    st.table(values_prpr)
            except:
                st.error("Error No Protein Found")

        elif choice == "Protein-Drug Interaction":

            st.header("Protein-Drug Interaction")
            tablepr_dr = init.table_pr_dr()
            with st.container():
                st.subheader("Table")
                st.dataframe(tablepr_dr)
                col1, col2 = st.columns([3, 1])
                col2.download_button(label="Download Table",
                                     data=tablepr_dr.to_csv().encode("utf-8"),
                                     file_name="table_pr_dr.csv")

            st.empty()
            with st.container():
                if st.button("Show Graph"):
                    st.subheader("Graph Of Table")
                    with st.spinner(text='In progress'):
                        fig_prdr = init.plot_graph(tablepr_dr)
                        st.pyplot(fig_prdr)
                        st.success("Graph is done")

            model_prdr = NodeVec().get_model("pr_dr.model")

            st.subheader("Interaction output")
            with st.container():
                try:
                    protein_name = st.text_input("Enter protein")

                    if len(protein_name) != 0:
                        values_prdr = NodeVec().returnSimilars(model_prdr, protein_name)
                        elements_pr_dr = init.printElements(
                            values_prdr, "P", item2="Q")
                        st.table(elements_pr_dr)
                except:
                    st.error("Error No Drug Found")

        elif choice == "Protein-Disease Interaction":

            st.header("Protein-Disease Interaction")
            table_prdi = init.table_dr_di()

            st.subheader("Table")
            with st.container():
                st.dataframe(table_prdi)
                col1, col2 = st.columns([3, 1])
                col2.download_button(label="Download Table",
                                     data=table_prdi.to_csv().encode("utf-8"),
                                     file_name="table_pr_dis.csv")
            with st.container():
                if st.button("Show Graph"):
                    st.subheader("Graph Of Table")
                    with st.spinner(text='In progress'):
                        fig_prdr = init.plot_graph(table_prdi)
                        st.pyplot(fig_prdr)
                        st.success("Graph is done")

            model_prdi = NodeVec().get_model("pr_dis.model")

            st.subheader("Interaction output")

            with st.container():
                try:
                    protein_name = st.text_input("Enter protein")

                    if len(protein_name) != 0:
                        values_prdi = NodeVec().returnSimilars(model_prdi, protein_name)
                        elements_pr_di = init.printElements(
                            values_prdi, "P", item2="Q")
                        st.table(elements_pr_di)
                except:
                    st.error("Error No Disease Found")

        elif choice == "Drug-Disease Interaction":

            st.header("Drug-Disease Interaction")
            table_drdi = init.table_dr_di()

            with st.container():
                st.subheader("Table")
                st.dataframe(table_drdi)
                col1, col2 = st.columns([3, 1])
                col2.download_button(label="Download Table",
                                     data=table_drdi.to_csv().encode("utf-8"),
                                     file_name="table_dr_dis.csv")

            with st.container():
                if st.button("Show Graph"):
                    st.subheader("Graph Of Table")
                    with st.spinner(text='In progress'):
                        fig_prdr = init.plot_graph(table_drdi)
                        st.pyplot(fig_prdr)
                        st.success("Graph is done")

            model_drdis = NodeVec().get_model("dr_dis.model")

            st.subheader("Interaction output")
            with st.container():
                try:
                    drug_name = st.text_input("Enter Drug")

                    if len(protein_name) != 0:
                        values_drdis = NodeVec().returnSimilars(model_drdis, protein_name)
                        elements_dr_dis = init.printElements2(
                            values_drdis, "DB")
                        st.table(elements_dr_dis)
                except:
                    st.error("Error No Disease Found")

        elif choice == "Drug-Drug Interaction":

            st.header("Drug-Drug Interaction")
            table_drdr = init.table_dr_dr()

            st.subheader("Table")
            with st.container():
                st.dataframe(table_drdr)
                col1, col2 = st.columns([3, 1])
                col2.download_button(label="Download Table",
                                     data=table_drdr.to_csv().encode("utf-8"),
                                     file_name="table_dr_dr.csv")

            with st.container():
                if st.button("Show Graph"):
                    st.subheader("Graph Of Table")
                    with st.spinner(text='In progress'):
                        fig_prdr = init.plot_graph(table_drdr)
                        st.pyplot(fig_prdr)
                        st.success("Graph is done")

            model_drdr = NodeVec().get_model("dr_dr.model")

            st.subheader("Interaction output")
            with st.container():
                try:
                    drug_name = st.text_input("Enter Drug")

                    if len(drug_name) != 0:
                        values_drdr = NodeVec().returnSimilars(model_drdr, drug_name)
                        st.table(values_drdr)
                except:
                    st.error("Error No Protein Found")

        elif choice == "Drug-Protein Interaction":
            st.header("Drug-Protein Interaction")
            table_drpr = init.table_dr_pr()

            with st.container():
                if st.button("Show Graph"):
                    st.subheader("Graph Of Table")
                    with st.spinner(text='In progress'):
                        fig_prdr = init.plot_graph(table_drpr)
                        st.pyplot(fig_prdr)
                        st.success("Graph is done")

            model_drpr = NodeVec().get_model("dr_pr.model")

            st.subheader("Interaction output")
            with st.container():
                try:
                    drug_name = st.text_input("Enter drug")

                    if len(drug_name) != 0:
                        values_drpr = NodeVec().returnSimilars(model_drpr, drug_name)
                        elements_dr_pr = init.printElements2(values_drpr, "DB")
                        st.table(elements_dr_pr)
                except:
                    st.error("Error No Protein Found")

        else:
            st.header("Drug-Side Effect Interaction")
            table_drse = init.table_dr_se()

            st.subheader("Table")
            with st.container():
                st.dataframe(table_drse)
                col1, col2 = st.columns([3, 1])
                col2.download_button(label="Download Table",
                                     data=table_drse.to_csv().encode("utf-8"),
                                     file_name="table_dr_se.csv")

            with st.container():
                if st.button("Show Graph"):
                    st.subheader("Graph Of Table")
                    with st.spinner(text='In progress'):
                        fig_prdr = init.plot_graph(table_drse)
                        st.pyplot(fig_prdr)
                        st.success("Graph is done")

            model_drdis = NodeVec().get_model("dr_dis.model")

            st.subheader("Interaction output")
            with st.container():
                try:
                    drug_name = st.text_input("Enter drug")

                    if len(drug_name) != 0:
                        values_drdis = NodeVec().returnSimilars(model_drdis, protein_name)
                        elements_dr_dis = init.printElements2(
                            values_drdis, "DB")
                        st.table(elements_dr_dis)
                except:
                    st.error("Error No Protein Found")


def main():

    str = Streamlit()
    str.streamlit()


if __name__ == "__main__":
    main()
