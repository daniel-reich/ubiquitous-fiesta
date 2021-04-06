
def darts_solver(sections, darts, target):
    ixs = [0] * darts
    i_ix = len(ixs)-1
    res = []
    while 1:
        curr_subset = [sections[i] for i in ixs]
        curr_sum = sum(curr_subset)
        if curr_sum >= target or ixs[i_ix] == len(sections)-1:
            if curr_sum == target:
                res.append(curr_subset)
            i = ixs[i_ix]
            i_ix -= 1
            while i_ix >= 0:
                if ixs[i_ix] < i:
                    ixs[i_ix] += 1
                    for j in range(i_ix+1, len(ixs)):
                        ixs[j] = ixs[i_ix]
                    i_ix = len(ixs) - 1
                    break
                i_ix -= 1
            if i_ix < 0:
                break
        else:
            # increment
            ixs[i_ix] += 1
    return ['-'.join([str(y) for y in x]) for x in sorted(res)]

