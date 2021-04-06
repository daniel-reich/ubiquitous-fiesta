
def zero_indices(seq, flips):
    '''
    Returns a list of the indices of 0s which when flipped up to flips times
    gives the longest sequence of 1s as per the instructions.
    '''
    from itertools import combinations, groupby
​
    flips = min(flips, seq.count(0))  # in case flips > num 0s in seq
    targets = [i for i in range(len(seq)) if seq[i] == 0] # indices of 0s
    flip_maxes = []  # store longest seq for each combo
    max_set = []  # store combo indices
​
    for combo in combinations(targets, flips):
        flipped_seq = [seq[i] if i not in combo else 1 for i in range(len(seq))]
        all_1s = [(k, len(list(v)))[1] for k, v in groupby(flipped_seq) \
                  if k == 1]
        flip_maxes.append(max(all_1s))
        max_set.append(list(combo))
​
    return max_set.pop(flip_maxes.index(max(flip_maxes)))

