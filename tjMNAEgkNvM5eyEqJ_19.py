
def unique_abbrev(abbs, words):
    a=[]
    if abbs[0]==words[1][:2] or abbs[0]==words[1][:2]:
        a.append('f')
    elif abbs[1]==words[0][:2] or abbs[1]==words[2][:2]:
        a.append('f')
    elif abbs[2]==words[0][:2] or abbs[2]==words[1][:2]:
        a.append('f')
    else:
        a.append('t')
    if 'f' in a:
        return False
    else:
        return True

