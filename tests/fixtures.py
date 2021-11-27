from src.search.graph_path_builder import GraphPathBuilder


class ExampleNode:
    def __init__(self, value):
        self.value = value
        self.neighbors = []

    def add_neighbor(self, node):
        self.neighbors.append(node)

    def __repr__(self):
        return str(self.value)

class GrapthPathBuilderForExampleNode(GraphPathBuilder):

    def __init__(self, dict_of_nodes):
        super().__init__()
        self.dict_of_nodes = dict_of_nodes

    def transverse(self, node_id):
        node = self.dict_of_nodes[node_id]
        return [n.value for n in node.neighbors]