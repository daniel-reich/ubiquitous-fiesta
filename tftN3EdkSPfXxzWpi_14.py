
def sentence_searcher(txt, n):
  if n<0:
    n = len(txt.split())+n
  txt = [[i,len(i.split())] for i in txt.split('. ')]
  start = 0
  for a,b in txt:
    if start<=n<start+b:
      return a+'.' if a[-1]!='.' else a
    else:
      start+=b

