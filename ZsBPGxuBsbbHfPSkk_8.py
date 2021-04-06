
def leaderboards(users):
    return sorted(users, key=lambda d: (d["score"]+d["reputation"]*2))[::-1]

