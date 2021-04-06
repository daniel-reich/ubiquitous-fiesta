
def completely_filled(lst):
    ans = []
    for line in lst:
        if ' ' in line:
            ans.append(False)
        else:
            ans.append(True)
    return all(ans)

