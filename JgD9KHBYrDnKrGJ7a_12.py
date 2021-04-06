
def swap_dict(dic):
    ans = {v:k for k,v in dic.items()}
    res = [[k,v]  for k,v in dic.items()]
    for k,v in ans.items():
        ans[k] =[i[0] for i in res if k in i]
    return ans

