
def tournament_scores(matches):
    scores = {team: [0, 0, 0, 0] for team in 'ABCD'}
    rewards = {1: (3, 0), -1:(0, 3)}
    for match in matches:
        A, gA, B, gB = match[0], int(match[2]), match[-1], int(match[-3])
        sA, sB = rewards.get(max(min(gA -gB, 1), -1), (1, 1))
        arrayA, arrayB = [sA, gA, gA -gB], [sB, gB, gB -gA]
        scores[A] = [acc +new for acc, new in zip(scores[A], arrayA)]
        scores[B] = [acc +new for acc, new in zip(scores[B], arrayB)]
    as_list = [[k, p1, p2, p3] for k, [p1, p2, p3] in scores.items()]
    return sorted(as_list, key=lambda x: x[1:], reverse=True)

