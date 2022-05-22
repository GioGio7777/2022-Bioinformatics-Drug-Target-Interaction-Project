from node2vec import Node2Vec
from gensim.test.utils import common_texts
from gensim.models import Word2Vec

class NodeVec:
    def node_2_vec(init,graph,save_name):
        node2vec = Node2Vec(graph,dimensions = 64,walk_length=800,num_walks = 10,weight_key="weight")
        model = node2vec.fit(batch_words=32)  
        model.save(save_name)
        return model

    def returnSimilars(init,model,value):
        return model.wv.most_similar(value)

    def get_model(init,model_name):
        model = "./models/" + model_name
        return Word2Vec.load(model)


    def printElements(init,output,item):
        elements = []
        for a in output:
            if a[0][0:2] != item:
                elements.append(a)
        return elements

    