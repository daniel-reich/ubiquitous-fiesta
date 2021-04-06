
def max_score(s):
  def splitter(string):
    splits = []
    
    for n in range(1, len(string)):
      splits.append([string[:n], string[n:]])
    
    return splits
  def score(split):
    
    left, right = split
    
    return left.count('0') + right.count('1')
  
  s = splitter(s)
  
  scores = [score(split) for split in s]
  
  return max(scores)

