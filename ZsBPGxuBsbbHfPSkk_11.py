
def leaderboards(users):
  for i in users: return (sorted(users, reverse=True, key=lambda i: i['score']+2*i['reputation']))

