from abc import ABC, abstractmethod
from typing import List, Tuple

class GraphPathBuilder(ABC):
    def __init__(self):
        """
        Initialize
        """
        self.graph_paths = []

    def _filter_list_by_value(self, list, value):
        """
        Filter list by value
        """
        return [item for item in list if item[-1] == value]

    def _remove_items_from_list_by_value(self, list, value):
        """
        Remove items from list by value
        """
        return [x for x in list if x != value]

    def visit(self, vertex, next_vertices):
        """
        Visit function
        """
        existing_paths = self._filter_list_by_value(self.graph_paths, vertex)
        new_paths = []
        if existing_paths:
            for path in existing_paths:
                for next_vertex in next_vertices:
                    new_paths = new_paths + [path + [next_vertex]]
            if new_paths:
                self.graph_paths = self._remove_items_from_list_by_value(self.graph_paths, path)
                self.graph_paths = self.graph_paths + new_paths
        else:
            for next_vertex in next_vertices:
                self.graph_paths= self.graph_paths + [[vertex] + [next_vertex]]

        return None

    @abstractmethod
    def transverse(self, node):
        ...
