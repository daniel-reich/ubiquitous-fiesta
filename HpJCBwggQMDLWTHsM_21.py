
def average_word_length(txt):
  if(txt == ""):
    return 0
  else:
    lst = list(txt.strip().split(' '))
    t = 0
    s = 0
    for elem in lst:
      kk = list(elem.strip())
      t += len(kk)
      if(kk[-1].isalpha()):
        t = t
      else:
        t -= 1
      s += 1
    T = float(t)
    S = float(s)
    p = float(float(T)/float(S))
    P = round(p,2)
    return P

