
def total_points(guesses, word):
    result = []
    for i in guesses:
        outcome = all([i.count(i[n]) <= word.count(i[n]) for n in range(len(i))])
        if outcome == True:
            if len(i) < 6:
                result.append(len(i) - 2)
            elif len(i) >= 6: 
                result.append(54)
        else:
            result.append(0)
    return sum(result)

