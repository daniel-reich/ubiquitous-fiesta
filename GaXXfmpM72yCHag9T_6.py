
def unique(lst):
    from collections import Counter
    y=[] 
    y=Counter(lst).most_common(2)
    item = [item for t in y for item in t]
    return (item[(len(item)-2)])

