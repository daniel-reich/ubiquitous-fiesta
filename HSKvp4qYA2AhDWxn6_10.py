
def total_points(guesses, word):
    points = 0
    for words in guesses:
        if len(words) == len(word):
            if sorted(words) == sorted(word):
                points += 54
        else:
            if sorted(words) == sorted([i for i in words if i in word and word.count(i) >= words.count(i)]) and len(words) == 3:
                points += 1
            if sorted(words) == sorted([i for i in words if i in word and word.count(i) >= words.count(i)]) and len(words) == 4:
                points += 2
            if sorted(words) == sorted([i for i in words if i in word and word.count(i) >= words.count(i)]) and len(words) == 5:
                points += 3
    return points

