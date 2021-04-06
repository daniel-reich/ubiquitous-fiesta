
def isWordChain(words):
  return all(isok(words[i],words[i+1]) for i in range(len(words)-1))
​
def isok(w1, w2):
  # ww is list of variation on word (1 letter missing)
  ww1 = [w1[:x] + w1[x+1:] for x in range(len(w1))]
  ww2 = [w2[:x] + w2[x+1:] for x in range(len(w2))]
  c1 = any(True for x in ww2 if x in ww1) # condition change letter
  c2 = any(True for x in ww2 if w1 == x) # condition add letter
  c3 = any(True for x in ww1 if w2 == x) # condition substract letter
  return any([c1, c2, c3])

