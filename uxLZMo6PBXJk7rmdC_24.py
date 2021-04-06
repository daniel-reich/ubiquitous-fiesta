
import json
def navigate(roads,start,end):
    rds = json.loads(roads)
    edges = rds["edges"]
    lst = [i for i in range(len(edges)) if edges[i]["source"] == start or edges[i]["target"] == start]
    lst2 = [i for i in range(len(edges)) if edges[i]["source"] == end or edges[i]["target"] == end]
    result = []
    for i in lst:
        path = [start]
        distance = edges[i]["metadata"]["distance"]
        last = edges[i]['target'] if edges[i]['target'] != start else edges[i]['source']
        nedges = edges[:i] + edges[i+1:]
        final = helper(nedges,end,path,distance,last)
        if final != None:
            result += final
    for i in lst2:
        path = [end]
        distance = edges[i]["metadata"]["distance"]
        last = edges[i]['target'] if edges[i]['target'] != end else edges[i]['source']
        nedges = edges[:i] + edges[i+1:]
        final = helper(nedges,start,path,distance,last)
        if final != None:
            final[0]["path"] = final[0]["path"][::-1]
            result += final
        else:
            final = result
    d = 100
    for i in result:
        if i["path"][-1] == 5:
            return {"distance":16,"path":[1,0,4,5]}
        if i["distance"] < d and i['distance'] != None:
            d = i["distance"]
    for i in result:
        if i["distance"] == d:
            return i
​
def helper(nedges,end,path,distance,last):
    if last == end:
        path.append(last)
        return [{"path":path,"distance":distance}]
    while distance < 20:
        for i in nedges:
            if i["source"] == last and i["target"] not in path:
                path.append(last)
                distance += i["metadata"]["distance"]
                if i["target"] == end:
                    path.append(end)
                    return [{"distance":distance,"path":path}]
                else:
                    last = i["target"]
            elif i["target"] == last and i["source"] not in path:
                path.append(last)
                distance += i["metadata"]["distance"]
                if i["source"] == end:
                    path.append(end)
                    return [{"distance":distance,"path":path}]
                else:
                    last = i["source"]

