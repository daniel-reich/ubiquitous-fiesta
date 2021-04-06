
def can_traverse(x):
    heights = [len(list(filter(bool, col))) for col in zip(*x)]
    return all(-1<=a-b<=1 for a,b in zip(heights, heights[1:]))

