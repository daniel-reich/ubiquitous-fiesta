
def pairs(lst):
  llst = len(lst)
  return [[a,b] for a,b in zip(lst[:(llst//2)+(llst%2)],lst[(llst//2):][::-1])]

