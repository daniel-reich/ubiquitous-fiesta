
def node_type(_N, _P, n):
    if n not in _N:
        return "Not exist"
    else:
        if n not in _P:
            return "Leaf"
​
        else:
            index = _N.index(n)
            if _P[index] == -1:
                return "Root"
            else:
                return "Inner"

