
def count_repetitions(items:list) -> dict:
    from collections import defaultdict
​
    reduced_items = list(set(items))
    counts = defaultdict(dict)
    for item in reduced_items:
        counts[item] = len([one for one in items if one == item])
​
    return dict(counts)

