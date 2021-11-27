from src.search.search import depth_first_trasverse
from src.search.graph_path_builder import GraphPathBuilder
from tests.fixtures import *


def test_depth_first_trasverse():
    # arrange
    root = ExampleNode(0)
    root.add_neighbor(ExampleNode(1))
    root.add_neighbor(ExampleNode(2))
    root.add_neighbor(ExampleNode(3))
    root.neighbors[0].add_neighbor(ExampleNode(4))
    root.neighbors[0].add_neighbor(ExampleNode(5))
    root.neighbors[0].neighbors[0].add_neighbor(ExampleNode(6))
    root.neighbors[0].neighbors[0].add_neighbor(ExampleNode(7))

    graph_dict = {}
    graph_dict[root.value] = root
    graph_dict[root.neighbors[0].value] = root.neighbors[0]
    graph_dict[root.neighbors[1].value] = root.neighbors[1]
    graph_dict[root.neighbors[2].value] = root.neighbors[2]
    graph_dict[root.neighbors[0].neighbors[0].value] = root.neighbors[0].neighbors[0]
    graph_dict[root.neighbors[0].neighbors[1].value] = root.neighbors[0].neighbors[1]
    graph_dict[root.neighbors[0].neighbors[0].neighbors[0].value] = root.neighbors[0].neighbors[0].neighbors[0]
    graph_dict[root.neighbors[0].neighbors[0].neighbors[1].value] = root.neighbors[0].neighbors[0].neighbors[1]


    graph_path_builder = GrapthPathBuilderForExampleNode(graph_dict)

    # act
    depth_first_trasverse(graph_path_builder.transverse, graph_path_builder.visit, root.value)

    # assert
    assert [0, 2] in graph_path_builder.graph_paths
    assert [0, 3] in graph_path_builder.graph_paths
    assert [0, 1, 5] in graph_path_builder.graph_paths
    assert [0, 1, 4, 6] in graph_path_builder.graph_paths
    assert [0, 1, 4, 7] in graph_path_builder.graph_paths
