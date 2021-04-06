
def leaderboards(users):
  return sorted(
    users,
    key = lambda user: 2 * user['reputation'] + user['score'],
    reverse = True,
  )

