
def total_points(guesses, word):
  return sum([len(j)-2 if all(j) and 3<=len(j)<=5 else 54 if all(j) and len(j)==6 else 0 for j in [[True if word.count(h)>=i.count(h) else False for h in list(i)] for i in guesses]])

