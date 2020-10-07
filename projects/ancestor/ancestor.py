import sys
sys.path.append("../graph/")
from graph import Graph

def earliest_ancestor(ancestors, starting_node):
    
    # Utilizing the graph class we already created
    graph = Graph()

    # Input data formatted as a list of (parent, child) pairs
    for parent, child in ancestors:
        graph.add_vertex(parent)
        graph.add_vertex(child)
        graph.add_edge(parent, child)

    for parent, child in ancestors:
        graph.add_edge(parent, child)

    target = None
    distance = 1

    for vertex in graph.vertices:

        lineage = graph.dfs(vertex, starting_node)

        if lineage:
            print(lineage)

            if len(lineage) > distance:
                distance = len(lineage)
                target = vertex

        elif not lineage and distance == 1:
            # If the input individual has no parents, we just return -1
            target = -1

    return target
