
def leaderboards(users):
  return sorted(users, key = lambda i: (i['score']+i['reputation']*2), reverse=True)

