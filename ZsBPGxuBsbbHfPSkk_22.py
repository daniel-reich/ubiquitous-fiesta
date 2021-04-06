
def leaderboards(users):
  return sorted(users, key=lambda u: u['reputation']*2 + u['score'], reverse=True)

