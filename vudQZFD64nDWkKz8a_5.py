
def grant_the_hint(txt):
  txt = txt.split()
  return [" ".join(w[:i]+"_"*(len(w)-i)for w in txt)for i in range(len(max(txt, key=len))+1)]

