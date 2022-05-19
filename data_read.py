import pandas as pd


class Read():
    def protein_read(init):
        return pd.read_csv("data/protein.txt", delim_whitespace=True, header=None, names=["Protein"])

    def protein_with_names(init):
        return pd.read_csv("data/protein_dict_map.txt", sep=":", header=None)

    def drug_read(init):
        return pd.read_csv("data/drug.txt", header=None, names=["Drug"])

    def drug_with_names_read(init):
        return pd.read_csv("data/drug_dict_map.txt", header=None)

    def disase_read(init):
        return pd.read_csv("data/disease.txt", header=None, names=["Disease"])

    def side_effects(init):
        return pd.read_csv("data/se.txt", header=None, names=["SideEffect"])

    def mat_protein_protein(init):
        pr_pr = pd.read_csv("data/mat_protein_protein.txt",
                            sep=" ", header=None)
        pr_pr.columns = init.protein_read()["Protein"].tolist()
        pr_pr["Protein"] = init.protein_read().Protein.tolist()
        pr_pr.set_index("Protein", inplace=True)
        pr_pr.reset_index(drop=True)
        return pr_pr

    def mat_protein_drug(init):
        pr_dr = pd.read_csv("data/mat_protein_drug.txt", sep=" ", header=None)
        pr_dr.columns = init.drug_read()["Drug"].tolist()
        pr_dr["Protein"] = init.protein_read().Protein.tolist()
        pr_dr.set_index("Protein", inplace=True)
        pr_dr.reset_index(drop=True)
        return pr_dr

    def mat_protein_disease(init):
        pr_dis = pd.read_csv(
            "data/mat_protein_disease.txt", sep=" ", header=None)
        pr_dis.columns = init.disase_read()["Disease"].tolist()
        pr_dis["Protein"] = init.protein_read().Protein.tolist()
        pr_dis.set_index("Protein", inplace=True)
        pr_dis.reset_index(drop=True)
        return pr_dis

    def mat_drug_disease(init):
        dr_dis = pd.read_csv("data/mat_drug_disease.txt", sep=" ", header=None)
        dr_dis.columns = init.disase_read()["Disease"].tolist()
        dr_dis["Drug"] = init.drug_read().Drug.tolist()
        dr_dis.set_index("Drug", inplace=True)
        dr_dis.reset_index(drop=True)
        return dr_dis

    def mat_drug_drug(init):
        dr_dr = pd.read_csv("data/mat_drug_drug.txt", sep=" ", header=None)
        dr_dr.columns = init.drug_read()["Drug"].tolist()
        dr_dr["Drug"] = init.drug_read().Drug.tolist()
        dr_dr.set_index("Drug", inplace=True)
        dr_dr.reset_index(drop=True)
        return dr_dr

    def mat_drug_protein(init):
        dr_pr = pd.read_csv("data/mat_drug_protein.txt", sep=" ", header=None)
        dr_pr.columns = init.protein_read()["Protein"].tolist()
        dr_pr["Drug"] = init.drug_read().Drug.tolist()
        dr_pr.set_index("Drug", inplace=True)
        dr_pr.reset_index(drop=True)
        return dr_pr

    def mat_drug_se(init):
        dr_se = pd.read_csv("data/mat_drug_se.txt", sep=" ", header=None)
        dr_se.columns = init.side_effects()["SideEffect"].tolist()
        dr_se["Drug"] = init.drug_read().Drug.tolist()
        dr_se.set_index("Drug", inplace=True)
        dr_se.reset_index(drop=True)
        return dr_se

    def drug_similarity_matrix(init):
        dr_sm = pd.read_csv(
            "data/Similarity_Matrix_Drugs.txt", sep="   ", header=None)
        dr_sm.columns = init.drug_read()["Drug"].tolist()
        dr_sm["Drug"] = init.drug_read().Drug.tolist()
        dr_sm.set_index("Drug", inplace=True)
        dr_sm.reset_index(drop=True)
        return dr_sm

    def protein_similarity_matrix(init):
        pr_sm = pd.read_csv(
            "data/Similarity_Matrix_Proteins.txt", sep=" ", header=None)
        pr_sm.columns = init.protein_read()["Protein"].tolist()
        pr_sm["Protein"] = init.protein_read().Protein.tolist()
        pr_sm.set_index("Protein", inplace=True)
        pr_sm.reset_index(drop=True)
        return pr_sm
