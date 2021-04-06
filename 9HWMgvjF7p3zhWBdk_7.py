
def keys_and_values(d):
    s_d = sorted(d)
    return [s_d, [d[s_d[i]] for i in range(len(d))]]

