
def climbing_leaderboard(ranked, player):
  
  class Person:
    
    def __init__(self, score, rank=None):
      self.score = score
      self.rank = rank
    # print(self.score, self.rank)
  class Leaderboard:
    
    def __init__(self, scores):
      
      self.s = list(reversed(sorted(list(set(scores)))))
      self.scores = scores
      
      self.ppl = []
      r = 1
      
      for score in self.s:
        c = scores.count(score)
        for n in range(c):
          self.ppl.append(Person(score, r))
        r += 1
    
    def rank(self, score):
      
      cr = 0
      ar = None
      
      for scor in self.s:
        if scor > score:
          for psn in self.ppl:
            if psn.score == scor:
              cr = psn.rank
              break
        elif scor == score:
          for psn in self.ppl:
            if psn.score == scor:
              ar = psn.rank
              break
          break
        else:
          break
      
      if ar != None:
        return ar
      else:
        return cr + 1
        
  leaderboard = Leaderboard(ranked)
  rankings = [leaderboard.rank(score) for score in player]
​
  return rankings

