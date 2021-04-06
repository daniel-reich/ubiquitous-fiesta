
def sentence_searcher(t,n):
  l=[(x.strip(),x.strip().count(' ')+1)for x in t.split('.')[:-1]]
  c,p=len(t.split(' ')),0
  if n<0:n+=c
  for x in l:
    p+=x[1]
    if p>=n+1:return x[0]+'.'

