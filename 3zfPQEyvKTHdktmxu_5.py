
def big_sub(lst):
    mss = [-float('inf')]
    start = 0
    current = 0
​
    for i, x in enumerate(lst):
        current = max(current+x, 0)
        if not current:
            start = i + 1
        if current >= mss[0]:
            mss = [current, start, i]
    
    return mss

