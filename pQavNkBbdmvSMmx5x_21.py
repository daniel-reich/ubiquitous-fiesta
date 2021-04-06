
def majority_vote(lst):
    if lst:
        d = {i:lst.count(i) for i in lst}
        max_key = max(d, key = d.get)
        max_value = max(d.values())
        if max_value > (len(lst)/2):
            return max_key
        else:
            return None
    else:
        return None

