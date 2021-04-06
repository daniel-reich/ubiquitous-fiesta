
def leaderboards(users):
  return sorted(users, key = lambda user: user['score']+2*user['reputation'])[::-1]

