
def find_split(a, split_into):
    if split_into == 1:
        return a
    if sum(a) % split_into != 0:
        return None
    check_val = sum(a) // split_into
    def check_func(path):
        return sum([a[i] for i in path]) == check_val
    q = [(0,(0,))]
    while q:
        # take from queue and check
        v = q.pop(0)
        if check_func(v[1]):
            # recursion
            a_new = [a[i] for i in range(len(a)) if i not in v[1]]
            next_split = find_split(a_new, split_into-1)
            if next_split:
                # return on recursion success
                curr_part = [a[i] for i in v[1]]
                return [curr_part] + [next_split]
        # append to queue 
        for w in range(v[0]+1, len(a)):
            q.append((w, v[1] + (w,)))
    return None
​
​
def coins_div(a):
    return find_split(a, 3) is not None

