
def shift_sentence(txt):
    txt = txt.split(' ')
    ans = list(list(i) for i in txt)
    first = ans[0][0]
    for i in range(len(ans)-1):
        ans[i+1][0],first=first,ans[i+1][0]
    ans[0][0]=first
    return " ".join(list("".join(i) for i in ans))

