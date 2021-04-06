
def all_about_strings(txt):
    ans = [len(txt), txt[0], txt[-1]]
    L = len(txt)
    if L % 2 == 0:
        ans.append(txt[L//2-1:L//2+1])
    else:
        ans.append(txt[L//2])
    second = txt[1]
    for i in range(2, len(txt)):
        if txt[i] == second:
            ans.append("@ index " + str(i))
            return ans
    ans.append("not found")
    return ans

