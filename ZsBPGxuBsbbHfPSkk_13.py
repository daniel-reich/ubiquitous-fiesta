
def leaderboards(users):
  trueScores = {}
  for u in users:
    trueScores[u["name"]] = u["score"] + u["reputation"] * 2
  return sorted(users, key=lambda x: trueScores[x["name"]], reverse=True)

