
def get_xp(d):
    scores = {"Very Easy": 5, "Easy": 10, "Medium": 20, "Hard": 40, "Very Hard": 80}
    return str(sum(scores.get(l) * d.get(l) for i, l in zip(d.keys(), scores.keys()))) + "XP"

