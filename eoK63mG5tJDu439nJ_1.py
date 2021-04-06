
def isWordChain(words):
  def chain(w1,w2):
    c1 = len(w1)==len(w2) and sum(w1[i]!=w2[i] for i in range(len(w1)))==1
    c2 = any(w1[:r]+w1[r+1:]==w2 for r in range(len(w1)))
    c3 = any(w2[:r]+w2[r+1:]==w1 for r in range(len(w2)))
    return c1 or c2 or c3
    
  return all(chain(words[i],words[i+1]) for i in range(len(words)-1))

