import pytest
from tests.fixtures import *


graph_path_builder = GrapthPathBuilderForExampleNode(None)

def test_remove_items_from_list_by_value():

    # act
    val1 = graph_path_builder._remove_items_from_list_by_value([1, 2, 3, 4, 5], 3)
    val2 = graph_path_builder._remove_items_from_list_by_value([[1, 2], [3, 4], [5]], [1,2]) 
    
    # assert
    assert val1 == [1, 2, 4, 5]
    assert val2 ==[[3, 4], [5]]

def test_visit_root():
    
    # arrange
    root = ExampleNode(0)
    root.add_neighbor(ExampleNode(1))
    root.add_neighbor(ExampleNode(2))
    root.add_neighbor(ExampleNode(3))
    root.neighbors[0].add_neighbor(ExampleNode(4))

    # act
    graph_path_builder.visit(root.value, [r.value for r in root.neighbors])

    # assert
    assert graph_path_builder.graph_paths == [[0, 1],[0, 2],[0, 3]]
