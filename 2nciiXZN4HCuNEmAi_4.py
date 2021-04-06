
def flatten(r):
    ans = []
    for item in r:
        if type(item) != list:
            ans.append(item)
        else:
            ans.extend(flatten(item))
    return ans

