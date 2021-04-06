
def fit_words(words, clue):
  ans = []
  for a in words:
    for b in [i for i in words if i!=a]:
      for c in [i for i in words if i not in [a,b]]:
        for d in [i for i in words if i not in [a,b,c]]:
          for e in [i for i in words if i not in [a,b,c,d]]:
            for f in [i for i in words if i not in [a,b,c,d,e]]:
              if c[3]==clue[1]:
                if a[0]==e[-1] and a[2]==c[4] and a[-1]==d[-1]:
                  if b[0]==c[0] and b[4]==d[2] and b[-1]==f[0]:
                    if c[2]==e[4] and c[-1]==f[-1]:
                      if d[0]==e[0] and d[4]==f[2]:
                        ans.append([a,b,c,d,e,f])
  return ans[-1]

