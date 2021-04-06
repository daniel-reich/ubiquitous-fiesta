
def get_xp(d):
    total, rank = 0, {"Very Easy": 5, "Easy": 10, "Medium": 20, "Hard": 40, "Very Hard": 80}
    for keys, values in d.items():
        total += rank.get(keys) * values
    return str(total) + "XP"

