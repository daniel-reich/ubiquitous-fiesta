
def swap_two(txt):
    ans = []
    while len(txt)>=4:
        ans.append(txt[2:4])
        ans.append(txt[0:2])
        txt=txt[4:]
    if(txt):
        ans.append(txt)
    return ''.join(ans)

