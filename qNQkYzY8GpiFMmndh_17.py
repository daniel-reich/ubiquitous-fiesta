
def overlap(w1, w2):
    lap = 0
    for i in range(min(len(w1), len(w2))):
        if w1[-(i + 1):] == w2[:i + 1]:
            lap = i + 1
    word = w1[:-lap] + w2 if lap else w1 + w2
    return word, lap
​
def join(lst):
    joint = lst[0]
    del lst[0]
    laps = []
    for i in lst:
        joint, lap = overlap(joint, i)
        laps.append(lap)
    return [joint, min(laps)]

