
def leaderboards(d):
  return [{"name": e[1], "score": e[2], "reputation": e[3]} for e in sorted([[e["score"]+e["reputation"]*2, e["name"], e["score"], e["reputation"]] for e in d], reverse=True)]

