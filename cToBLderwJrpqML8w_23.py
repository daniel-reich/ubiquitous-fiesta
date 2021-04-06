
def champions(lst):
    highest_score = 0
    largest_diff = 0
    current = None
    for di in lst:
        score =  (3 * di['wins']) + (1 * di['draws'])
        diff = di['scored'] - di['conceded']
        if score >= highest_score:
            if score == highest_score:
                if diff > largest_diff:
                    current, largest_diff, highest_score = di['name'], diff, score 
            else:
                current, largest_diff, highest_score = di['name'], diff, score
    return current

