
def leaderboards(users):
  return sorted(users,key=lambda x: x['score']+2*x['reputation'],reverse=True)

