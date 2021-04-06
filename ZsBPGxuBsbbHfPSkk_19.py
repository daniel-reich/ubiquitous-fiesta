
def leaderboards(users):
  users.sort(key=lambda di: di['reputation'] * 2 + di['score'], reverse=True)
  return users

