
import json
import os
​
​
def neighbours_of(edges, node):
    neighbours = []
    for edge in edges:
        if node in edge:
            neighbours.append(edge[0 if edge[1] == node else 1])
    return neighbours
​
​
def node_pop(iter, func):
    minimum = min(iter, key=func)
    iter.remove(minimum)
    return minimum, func(minimum)
​
​
def navigate(graph, startingNode, endingNode):
    # parse the graph
    graph_dict = json.loads(graph)
    node_ids = [node["id"] for node in graph_dict["nodes"]]
    edges = {}
    for edge_dict in graph_dict["edges"]:
        edge_a = edge_dict["source"]
        edge_b = edge_dict["target"]
        if edge_a not in node_ids or edge_b not in node_ids:
            continue
        distance = edge_dict["metadata"]["distance"]
        edges[(edge_a, edge_b)] = distance
        edges[(edge_b, edge_a)] = distance
​
    # find the shortest path
    distances = {startingNode: 0}
    queue = []
    predecessors = {}
    for node in node_ids:
        if node is not startingNode:
            distances[node] = float('inf')
        predecessors[node] = None
        queue.append(node)
​
    while queue:
        lowest_node_id, lowest_node_distance = node_pop(queue, lambda x: distances[x])
        if lowest_node_id == endingNode:
            break
        for neighbour in filter(lambda x: x in queue, neighbours_of(edges, lowest_node_id)):
            tentative = lowest_node_distance + edges[(neighbour, lowest_node_id)]
            if tentative < distances[neighbour]:
                distances[neighbour] = tentative
                predecessors[neighbour] = lowest_node_id
​
    path = []
    current = endingNode
    result_distance = 0
    while current in predecessors:
        path.insert(0, current)
        if predecessors[current] is not None:
            result_distance += edges[(current, predecessors[current])]
        current = predecessors[current]
​
    output = {
        "distance": result_distance,
        "path": path
    }
    return output

