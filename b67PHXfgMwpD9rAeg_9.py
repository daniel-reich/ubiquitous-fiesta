
def plus_sign(txt):
    if txt[0].isalpha() :
        return False
    return sum(map(lambda x : 1 if x.isalpha() else 0,txt))==sum(True for m in
      [r for r in enumerate( txt) if r[1].isalpha() ] if txt[m[0]-1]=='+' and txt[m[0]+1]=='+')

