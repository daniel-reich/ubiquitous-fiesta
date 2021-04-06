
def leaderboards(users):
  return sorted(users, key=lambda u: u['score'] + u['reputation'] * 2, reverse=True)

