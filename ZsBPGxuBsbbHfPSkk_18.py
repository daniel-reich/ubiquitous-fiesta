
def leaderboards(users):
  def score(user):
    return user["score"]+2*user["reputation"]
  return sorted(users,key=score)[::-1]

