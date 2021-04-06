
def grant_the_hint(txt):
  return [' '.join(j[:i].ljust(len(j),'_') for j in txt.split()) for i in range(max(len(i) for i in txt.split())+1)]

