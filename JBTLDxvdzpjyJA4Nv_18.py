
def dfs(txt, ans):
    if len(txt) <= 1:
        return ans if len(ans) > 0 else "Empty String"
    for i in range(1, len(txt)):
        if txt[i-1] == txt[i]:
            txt2 = txt[:i-1] + txt[i+1:]
            if len(txt2) < len(ans):
                ans = txt2
            ans = dfs(txt2, ans)
    return ans if len(ans) > 0 else "Empty String"
​
def super_reduced_string(txt):
    return dfs(txt, txt)

