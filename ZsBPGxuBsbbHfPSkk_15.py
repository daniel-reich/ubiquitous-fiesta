
def leaderboards(users):
  return sorted(users, key=lambda x: -(x["score"] + x["reputation"] * 2))

