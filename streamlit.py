import streamlit as st
from data_read import Read
from network import Network
from node_2_vec import NodeVec


class Streamlit:
    def table_protein(init):
        read = Read()
        return read.mat_protein_protein()

    def table_pr_dr(init):
        read = Read()
        return read.mat_protein_drug()

    def table_pr_di(init):
        read = Read()
        return read.mat_protein_disease()

    def table_dr_dr(init):
        read = Read()
        return read.mat_drug_drug()

    def table_dr_pr(init):
        read = Read()
        return read.mat_drug_protein()

    def table_dr_se(init):
        read = Read()
        return read.mat_drug_se()

    def table_dr_di(init):
        read = Read()
        return read.mat_protein_disease()

    def streamlit(init):
        st.title("Bionfo Project")

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

        elif choice == "Protein-Drug Interaction":

            st.header("Protein-Drug Interaction")
            tablepr_dr = init.table_pr_dr()

            st.subheader("Table")
            st.dataframe(tablepr_dr)

        elif choice == "Protein-Disease Interaction":

            st.header("Protein-Disease Interaction")
            table_prdi = init.table_dr_di()

            st.subheader("Table")
            st.dataframe(table_prdi)

        elif choice == "Drug-Disease Interaction":

            st.header("Drug-Disease Interaction")
            table_drdi = init.table_dr_di()

            st.subheader("Table")
            st.dataframe(table_drdi)

        elif choice == "Drug-Drug Interaction":

            st.header("Drug-Drug Interaction")
            table_drdr = init.table_dr_dr()

            st.subheader("Table")
            st.dataframe(table_drdr)

        elif choice == "Drug-Protein Interaction":
            st.header("Drug-Protein Interaction")
            table_drpr = init.table_dr_pr()

        else:
            st.header("Drug-Side Effect Interaction")
            table_drse = init.table_dr_se()

            st.subheader("Table")
            st.dataframe(table_drse)


def main():

    str = Streamlit()
    str.streamlit()


if __name__ == "__main__":
    main()
