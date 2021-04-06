
def leaderboards(users):
  return sorted(users, key=lambda i:i['reputation']*2+i['score'], reverse=True)

