
def cutting_grass(lst, *cuts):
    if any(x == 0 for x in lst):
        return ['Done'] * len(cuts)
​
    grass_cuts, c, i = [lst], 0, 0
    while any(x != 0 for x in cuts) and i < len(cuts):
        if any(cuts[c] == x for x in lst):
            return ['Done'] * len(lst)
        heights = [n - cuts[c] for n in grass_cuts[-1]]
        i += 1
        c += 1
        if any(x == 0 for x in heights):
            grass_cuts.append('Done')
            break
        grass_cuts.append(heights)
    return grass_cuts[1:]

