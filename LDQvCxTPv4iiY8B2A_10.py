
def same_upsidedown(a):
    return False not in [a[i] == {'6':'9','9':'6','0':'0'}.get(a[::-1][i]) for i in range(len(a))]

