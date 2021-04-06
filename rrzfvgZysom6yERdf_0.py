
SEQUENCE = "23456789TJQKA"
​
VALUES = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
          'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
​
def get_score(hand):
    BASE = 1000000
    colors = [h[1] for h in hand]
    faces = [h[0] for h in hand]
    values = [VALUES[f] for f in faces]
    counts = {face: faces.count(face) for face in faces}
    #
    # straight flush:
    max_value, min_value = max(values), min(values)
    if len(list(set(colors))) == 1 and \
       sorted(values) == list(range(min_value, max_value + 1)):
        return 9 * BASE + max(values)
    #
    # four of a kind:
    if 4 in counts.values():
        for f in counts:
            if counts[f] == 4:
                return 8 * BASE + VALUES[f]
    #
    # full house:
    if 2 in counts.values() and 3 in counts.values():
        for f in counts:
            if counts[f] == 3:
                return 7 * BASE + VALUES[f]
    #
    # flush:
    if len(list(set(colors))) == 1:
        values = sorted(values, reverse=True)
        return 6 * BASE + 16**4 * values[0] + 16**3 * values[1] + \
               16**2 * values[2] + 16**1 * values[3] + 16**0 * values[4]
    #
    # straight:
    if sorted(values) == list(range(min_value, max_value + 1)):
        return 5 * BASE + max(values)
    #
    # three of a kind:
    if 3 in counts.values():
        for f in counts:
            if counts[f] == 3:
                return 4 * BASE + VALUES[f]
    #
    # two pairs:
    if sorted(counts.values()) == [1, 2, 2]:
        a = -1
        for f in faces:
            if counts[f] == 1:
                c = VALUES[f]
            else:
                if a == -1:
                    a = VALUES[f]
                else:
                    b = VALUES[f]
        if a < b:
            a, b = b, a
        return 3 * BASE + 256 * a + 16 * b + c
    #
    # one pair:
    if 2 in counts.values():
        other = []
        for f in faces:
            if counts[f] == 2:
                a = VALUES[f]
            else:
                other.append(VALUES[f])
        other = sorted(other, reverse=True)
        return 2 * BASE + 4096 * a + 256 * other[0] + 16 * other[1] + other[2]
    #
    # high card:
    values = sorted(values, reverse=True)
    return 16**4 * values[0] + 16**3 * values[1] + 16**2 * values[2] + \
           16 * values[3] + values[4]
​
def player1_wins(lst):
    wins1 = 0
    for game in lst:
        score1 = get_score(game.split()[:5])
        score2 = get_score(game.split()[5:])
        if score1 > score2:
            wins1 += 1
    return wins1

