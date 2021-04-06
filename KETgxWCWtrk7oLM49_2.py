
class Team():
  def __init__(self, t, p, g, d):
    self.t = t
    self.p = p
    self.g = g
    self.d = d
  def __repr__(self):
    return self.t
  def __lt__(self, other):
    if self.p > other.p:
      return True
    elif other.p > self.p:
      return False
    if self.g > other.g:
      return True
    elif other.g > self.g:
      return False
    if self.d > other.d:
      return True
    return False
​
def tournament_scores(lst):
  teams = {}
  for i in lst:
    t1 = i[0]
    g1 = int(i[2])
    g2 = int(i[6])
    t2 = i[-1]
    if g1 > g2:
      p1 = 3
      p2 = 0
    elif g1 == g2:
      p1 = 1
      p2 = 1
    else:
      p1 = 0
      p2 = 3
    if t1 not in teams:
      teams[t1] = {'Points':p1, 'Goals': g1, 'Differential':g1-g2}
    else:
      teams[t1]['Points'] += p1
      teams[t1]['Goals'] += g1
      teams[t1]['Differential'] += g1-g2
    if t2 not in teams:
      teams[t2] = {'Points':p2, 'Goals': g2, 'Differential':g2-g1}
    else:
      teams[t2]['Points'] += p2
      teams[t2]['Goals'] += g2
      teams[t2]['Differential'] += g2-g1
  output = [Team(i, teams[i]['Points'], teams[i]['Goals'], teams[i]['Differential']) for i in teams]
  output.sort()
  output2 = [[i.t, i.p, i.g, i.d] for i in output]
  return output2

