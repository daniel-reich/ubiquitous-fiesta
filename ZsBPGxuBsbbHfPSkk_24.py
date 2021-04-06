
def leaderboards(users):
    return sorted(users, key=lambda x: x.get('score') + x.get('reputation')*2, reverse=True)

