
def currently_winning(scores):
  y,o = scores[::2], scores[1::2]
  y = [sum(y[:i]) for i in range(1, len(y)+1)]
  o = [sum(o[:i]) for i in range(1, len(o)+1)]
  return ["T" if i==j else "Y" if i>j else "O" for i,j in zip(y,o)]

