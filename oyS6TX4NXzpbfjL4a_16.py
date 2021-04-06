
def points(board, word):
  pointvalues = {"a":1,"b":3,"c":3,"d":2,"e":1,"f":4,"g":2,"h":4,"i":1,"j":8,"k":5,"l":2,"m":3,"n":1,"o":1,"p":3,"q":10,"r":1,"s":1,"t":1,"u":1,"v":4,"w":4,"x":8,"y":4,"z":10}
  multipliers = {"-":1, "DW":1, "DL":2, "TL":3}
  score = 0
  for i in range(len(word)):
    score += pointvalues[word[i]] * multipliers[board[i]]
  if "DW" in board:
    score *= 2
  return score
    
def best_start(lst, word):
  bestscore = 0
  bestindex = 0
  for i in range(len(lst) - len(word)):
    score = points(lst[i:i+len(word)], word)
    if score > bestscore:
      bestscore = score
      bestindex = i
  return bestindex

