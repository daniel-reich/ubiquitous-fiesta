
def extract_num(el):
    ans = 0
    s = ''.join([c if c == '-' or '0' <= c <= '9' else ' ' for c in el]).replace('-', ' -')
    for k in s.split():
        if len(k) > 0 and k.strip() != '-':
            ans += int(k)
    return ans
    
def dfs(L, ans):
    if len(L) == 0:
        return ans
    for el in L:
        if type(el) == list:
            ans = dfs(el, ans)
        else:
            ans += extract_num(el)
    return ans
​
def deep_sum(lst):
    return dfs(lst, 0)

