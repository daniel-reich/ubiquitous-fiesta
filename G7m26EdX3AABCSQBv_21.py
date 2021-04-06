
def format_ascii(txt, width):
    ans=txt[0]
    for i in range(1,len(txt)):
        if i % width == 0:
            ans+=("\n"+txt[i])
        else:
            ans+=txt[i]
    return ans

