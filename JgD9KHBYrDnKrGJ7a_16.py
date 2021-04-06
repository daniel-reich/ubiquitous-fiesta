
def swap_dict(dic):
    ans = {}
    for k, v in dic.items():
        if v in ans:
            ans[v].append(k)
        else:
            ans[v] = [k]
    return ans

