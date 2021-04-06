
def total_points(guesses,word):
  pts = 0
  for i in guesses:
    if len(i) > 2:
      for j in i:
        if i.count(j) > word.count(j):
          break
      else:
        pts += len(i)-2
        if len(i)==6:
          pts += 50
  return pts

