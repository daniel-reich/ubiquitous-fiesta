
def node_type(_N, _P, n):
    if n in _N:
        if n in _P:
            indx = _N.index(n)
            if _P[indx] == -1:
                return "Root"
            else:
                return "Inner"
        else:
            return "Leaf"
    else:
        return "Not exist"

