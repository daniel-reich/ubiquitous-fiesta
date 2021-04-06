
def leaderboards(users):
    return sorted(users, key=lambda x: ((x["reputation"] * 2) + x["score"]), reverse=True)

