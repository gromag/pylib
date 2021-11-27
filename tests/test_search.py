from src.search.search import depth_first_trasverse
from src.search.graph_path_builder import GraphPathBuilder
from tests.fixtures import *
from pandas import DataFrame


def test_depth_first_trasverse_with_tree_structure():
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


def test_depth_first_trasverse_with_dataframe():
    # arrange
    PARENT = "parent"
    CHILD = "child"
    df = DataFrame([[0,1],[0,2],[0,3],[1,4],[1,5],[4,6],[4,7]], columns=[PARENT, CHILD])
    graph_path_builder = GrapthPathBuilderForExampleDataframe(df, PARENT, CHILD)

    # act
    depth_first_trasverse(graph_path_builder.transverse, graph_path_builder.visit, 0)

    # assert
    assert [0, 2] in graph_path_builder.graph_paths
    assert [0, 3] in graph_path_builder.graph_paths
    assert [0, 1, 5] in graph_path_builder.graph_paths
    assert [0, 1, 4, 6] in graph_path_builder.graph_paths
    assert [0, 1, 4, 7] in graph_path_builder.graph_paths


def test_depth_first_trasverse_with_cyclical_graph():

        # arrange
    PARENT = "parent"
    CHILD = "child"
    # cyclical graph the 7 child column is a parent of 0
    df = DataFrame([[0,1],[0,2],[0,3],[1,4],[1,5],[4,6],[4,7],[7,0]], columns=[PARENT, CHILD])
    graph_path_builder = GrapthPathBuilderForExampleDataframe(df, PARENT, CHILD)

    # act
    depth_first_trasverse(graph_path_builder.transverse, graph_path_builder.visit, 0)

    # assert
    assert [0, 2] in graph_path_builder.graph_paths
    assert [0, 3] in graph_path_builder.graph_paths
    assert [0, 1, 5] in graph_path_builder.graph_paths
    assert [0, 1, 4, 6] in graph_path_builder.graph_paths
    assert [0, 1, 4, 7] in graph_path_builder.graph_paths