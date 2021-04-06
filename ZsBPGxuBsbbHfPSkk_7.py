
def leaderboards(users):
    return [el[0] for el in sorted([[user, user["score"]+2*user["reputation"]] for user in users], key=lambda x:-x[1])]

