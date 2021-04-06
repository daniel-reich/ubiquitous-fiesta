
def mystery_func(txt):
    ans = ""
    for i in range(0, len(txt)):
        if i%2 != 0:
            ans = ans + txt[i-1]*int(txt[i])
    return ans

