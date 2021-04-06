
def can_patch(bridge, planks):
    '''
    Returns True if holes in the bridge can be repaired with any of the planks,
    as explained in the instructions.
    '''
    from itertools import groupby
​
    holes = sorted([(k,len(list(v)))[1] for k, v in groupby(bridge) \
                    if k==0], reverse=True)
    holes = holes if holes.count(1) == 0 else holes[:holes.index(1)] #drop singles
​
    return len(planks) >= len(holes) and \
           all(b >= a-1 for a, b in zip(holes, sorted(planks, reverse=True)))

