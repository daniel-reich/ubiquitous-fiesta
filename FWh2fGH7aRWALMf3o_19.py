
def C(string, lst, res, i=0):
    if i == len(string): return True
    for w in filter(lambda w: w.startswith(string[i]), lst):
        if string[i:i+len(w)] == w:
            if C(string, lst, res, i+len(w)):
                res.insert(0, w)
                return True
    return False
        
def cleave(string, lst):
    res = []
    return ' '.join(res) if C(string, lst, res) else "Cleaving stalled: Word not found"

