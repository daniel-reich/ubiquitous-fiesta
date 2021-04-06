
def award_prizes(names):
    temp = names.items()
    temp = sorted([(x, y) for y, x in temp], reverse=True)
    prizes = ["Gold", "Silver", "Bronze", "Participation"] + (len(names) - 4) * ["Participation"]
    names = {y[1] : z for  y, z in (zip(temp, prizes))}
    return names

