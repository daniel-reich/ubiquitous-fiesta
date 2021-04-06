
def pilish_string(s):
  pi, r, k = [int(d) for d in '314159265358979'], [], 0
  for i in pi:
    r.append(s[k:k+i]) if s[k:k+i] else r
    k += i
  return '' if not r else ' '.join(r) if len(r[-1]) == pi[len(r)-1] \
    else ' '.join(r[:-1]+[r[-1]+r[-1][-1]*(pi[len(r)-1]-len(r[-1]))])

