
def sort_by_string(lst, txt):
    ans = []
    for x in txt:
        for w in lst:
            if w[0] == x:
                ans.append(w)
                break
    return ans

