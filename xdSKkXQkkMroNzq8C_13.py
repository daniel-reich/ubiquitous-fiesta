
def count_d(sentence):
    a = 0
    for h in range(len(sentence)):
        if sentence[h].lower() == "d":
            a += 1
    return a

