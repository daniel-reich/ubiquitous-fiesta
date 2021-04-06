
def leaderboards(users):
      return sorted(users, key=lambda d: d['reputation'] * 2 + d['score'], reverse=True)

