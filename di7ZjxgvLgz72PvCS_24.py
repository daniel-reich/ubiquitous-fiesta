
def validate_swaps(values, target):
    '''
    Returns a list of booleans: True if val in values can be formed from target
    by a single swap of 2 character, False otherwise.
    '''
    POSITIONS = {i: target[i] for i in range(len(target))}
    result = []
​
    for val in values:
        if len(val) != len(target) or any(val.count(l) > 1 for l in val):
            swap = False   # must be same length & no duplicates
        else:
            val_idxs = [val.find(char) for _, char in POSITIONS.items()]
            swap = sum(1 for i in range(len(val_idxs)) if val_idxs[i] == sorted(POSITIONS)[i])
            swap = swap == len(target) - 2  # 2 will be different if 1 swap occurred
        result.append(swap)
​
    return result

