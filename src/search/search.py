
def depth_first_trasverse(transverseToNextNodesFn, visitFn, start):
    """
    Depth first trasverse, can be used to search or traverse a graph
    based on visitFn implementation.
    """
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        visited.add(vertex)
        next_vertices = transverseToNextNodesFn(vertex)
        next_vertices = [v for v in next_vertices if v not in visited]
        found = visitFn(vertex, next_vertices)
        if found:
            return found
        stack.extend(next_vertices)
    return None

