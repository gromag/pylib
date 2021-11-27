
def depth_first_trasverse(transverseToNextNodesFn, visitFn, start):
    """
    Depth first trasverse, can be used to search or traverse a graph
    based on visitFn implementation.
    """
    stack = [start]
    while stack:
        vertex = stack.pop()
        next_vertices = transverseToNextNodesFn(vertex)
        found = visitFn(vertex, next_vertices)
        if found:
            return found
        stack.extend(next_vertices)
    return None
