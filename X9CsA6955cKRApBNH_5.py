
def longest_run(lst):
    x = run(lst, 1)
    y = run(lst, -1)
    return max(x,y)
​
def run(lst, d):
    lor = []
    r = 1
    prev = lst[0]
    for x in lst[1:]:
        if x - prev == d:
            prev = x
            r += 1
        else:
            lor.append(r)
            prev = x
            r = 1
    lor.append(r)
    return max(lor)

