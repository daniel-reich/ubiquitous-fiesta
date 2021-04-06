
def recur_index(txt):
    if txt == None:
      return {}
    return recur_index_tmp(txt, {}, 0)
  
def recur_index_tmp(txt, dict, n):
    if len(txt) == n:
        return {}
    t = txt[n]
    if t in dict:
        dict[t].append(n)
        return {t: dict[txt[n]]}
    else:
        dict.setdefault(t, [n])
        return recur_index_tmp(txt, dict, n+1)

