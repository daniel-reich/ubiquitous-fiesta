
import json
def navigate(roads_str, source, destination):
    
    roads = json.loads(roads_str)
    #print(roads)
​
    nodes = roads["nodes"]
    nodes_total = len(nodes)
    edges = roads["edges"]
     
    
    nodes_prev = [-1]*(nodes_total)
    
    nodes_dist = [-1]*(nodes_total)
    nodes_dist[source] = 0
​
    working_list = []
    for i in range(nodes_total):
        working_list.append(i)
    length = len(working_list)
    while(length != 0):
        min_index = working_list[0]
        min_dist = nodes_dist[min_index]
        working_node = -1
        for i in range(length):
            if working_list[i] != -1:
                
                if min_dist == -1 or (min_dist > nodes_dist[working_list[i]] and nodes_dist[working_list[i]] != -1):
                    
                    min_index = working_list[i]
                    min_dist = nodes_dist[min_index]
        if min_dist != -1:
            
            working_node = min_index
 
            working_list.remove(min_index) 
            for edge in edges:
                neighbor_node = -1
                if working_node == edge["source"]:
                    neighbor_node = edge["target"]
                    
                elif working_node == edge["target"]:
                    neighbor_node = edge["source"]
                    
                if neighbor_node != -1:
                    if nodes_dist[working_node] + edge["metadata"]["distance"] < nodes_dist[neighbor_node] or nodes_dist[neighbor_node] == -1:
                        nodes_dist[neighbor_node] = nodes_dist[working_node] + edge["metadata"]["distance"]
                        nodes_prev[neighbor_node] = working_node
  
        else:
            break
        length = len(working_list)
    
​
    result = {}
    result["distance"] = 0
    result["path"] = []
    
    result["distance"] = nodes_dist[destination]
    current = destination
    while current != -1:
        result["path"].append(current)
        current = nodes_prev[current]
    result["path"].reverse()
    return result

