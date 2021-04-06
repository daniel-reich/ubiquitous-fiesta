
def majority_vote(lst):
    each = list(set(lst))
    n, ne = len(lst), len(each)
    scores = [lst.count(score) for score in each]
    if (n == 0 or
            (ne == 1 and lst.count(lst[0]) < 1)) or\
            (ne > 1 and scores[0] == scores[1]) or\
            max(scores) < n / 2:
        return None
    else:
        return each[scores.index(max(scores))]

