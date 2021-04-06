
def total_points(guesses, word):
    total = 0
    lst = guesses
​
    for i in range(len(lst)):
        guess = sorted(lst[i])
        if len(guess) == len(word) and guess != sorted(word):
            total += 0
        elif len(guess) == len(word):
            total += 54
        else:
            tot = 0
            for j in lst[i]:
                if lst[i].count(j) > word.count(j) or j not in word:
                    tot = 0
                    break
                elif j in word:
                    tot += 1
​
            if tot < 3:
                tot = 0
            elif tot < 6:
                tot -= 2
​
            total += tot
​
    return total

