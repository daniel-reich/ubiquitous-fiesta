
def award_prizes(scores: dict) -> dict:
    medals = ['Gold', 'Silver', 'Bronze', 'Participation']
    awards = sorted(scores.values(), reverse=True)
    for key in scores:
        i = awards.index(scores[key])
        if i > 2:
            scores[key] = 'Participation'
        else:
            scores[key] = medals[i]
    return scores

