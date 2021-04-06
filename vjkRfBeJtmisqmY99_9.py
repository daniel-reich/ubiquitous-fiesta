
class Constraint:
  def __init__(self, srcPos, target, targetPos):
    self.locIdx = srcPos
    self.target = target
    self.targetIdx = targetPos
  def check(self, word, wordList):
    return word[self.locIdx - 1] == wordList[self.target - 1][self.targetIdx - 1]
    
constraints = ( (), #w1 
               (), #w2
               (Constraint(1, 2, 1), Constraint(5, 1, 3)), #w3
               (Constraint(3, 2, 5), Constraint(7, 1, 7)), #w4
               (Constraint(1, 4, 1), Constraint(5, 3, 3), Constraint(7, 1, 1)), #w5
               (Constraint(1, 2, 7), Constraint(3, 4, 5), Constraint(7, 3, 7)) ) #w6
​
​
def fit_lvl(words, seq, lvl, mid):
  if lvl >= 6:
    return True
  options = [w for w in words if (w not in seq) and \
                        all(c.check(w, seq) for c in constraints[lvl]) and \
                        (w[3] == mid[1] if lvl == mid[0]-1 else True )]
  #print(lvl, ']',seq, ' -> ', options)
  if not options:
    return False
  for op in options:
    seq.append(op)
    valid = fit_lvl(words, seq, lvl + 1, mid)
    if valid:
      return True
    seq.pop()
  return False
  
def fit_words(words, clue):
  seq  = []
  possible = fit_lvl(words, seq, 0, clue)
  if possible:
    return seq
  else:
    return None

