
chain=[[[0,4,-1],[2,2,4],[-1,3,-1]],[[0,2,0],[4,3,2],[-1,5,0]],
        [[0,1,0],[2,4,4],[4,0,2],[-1,5,-1]],[[0,4,0],[2,1,4],[4,5,2],[-1,0,-1]],
  [[0,3,0],[4,2,2],[-1,0,0]],[[0,1,-1],[2,3,4],[-1,2,-1]]]
ansx=[]
​
def fit_words(words, clue):
  global chain,ansx
  for i in [w for w in words if w[len(w)//2]==clue[1]]:
    check(i,words,[[clue[0]-1,i]],clue[0]-1)
  mem,ansx=ansx,[]
  return mem[0] if len(mem)==1 else mem
​
def check(word,pool,res,con):
  global chain,ansx
  pool.remove(word);
  dic={i:w for i,w in res};n=-2
  while all([i[1] in dic and dic[i[1]][i[2]]==word[i[0]] for i in chain[con]]):
    try:con,word=res[n];n-=1
    except:
      mem = [w for i,w in sorted(res,key = lambda x:x[0])]
      if mem not in ansx:ansx+=[mem]
      break
  for i in chain[con]:
    if i[1] in dic and dic[i[1]][i[2]]!=word[i[0]]:break
    elif i[1] in dic:pass
    else:
      memw = [w for w in pool if w[i[2]]==word[i[0]]]
      if not memw:break
      for j in memw:check(j,pool[:],res[:]+[[i[1],j]],i[1])

