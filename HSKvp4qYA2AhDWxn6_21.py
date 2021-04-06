
def total_points(guesses, word):
    count=0
    for x in guesses:
        if sorted(x)==sorted(word):
            count+=50
        for y in x:
            if x.count(y)>word.count(y):
                guesses.remove(x)
                break
    for x in guesses:
        count+=len(x)-2  
    return count

