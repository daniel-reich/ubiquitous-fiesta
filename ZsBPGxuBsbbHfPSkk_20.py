
def leaderboards(users):
  return sorted(users, key=lambda u: u['score'] + 2 * u['reputation'], reverse=True)

