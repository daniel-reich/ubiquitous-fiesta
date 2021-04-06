
def trace_word_path(word, grid):
  
  
  def test(w,a,b,ll):
    if a<0 or b<0 or a>=len(grid) or b>=len(grid[0]) or (a,b) in ll: return []
    if grid[a][b]!=w[0]: return []
​
    if len(w)<2: return [(a,b)]
    
    for i in range(4):
      if i==0:
        tmp=test(w[1:],a-1,b,ll+[(a,b)])
      elif i==1:
        tmp=test(w[1:],a+1,b,ll+[(a,b)])
      elif i==2:
        tmp=test(w[1:],a,b-1,ll+[(a,b)])
      else:
        tmp=test(w[1:],a,b+1,ll+[(a,b)])
      if len(tmp)==len(w)-1:
        return [(a,b)]+tmp
    return []
      
​
  for i in range(len(grid)):
    for j in range(len(grid[0])):
      tmp=test(word,i,j,[])
      print('*',i,j,tmp)
      if len(tmp)==len(word):
        return tmp
  return 'Not present'

