
def mine_run(tracks):
    v = float(0)
    for i in range(len(tracks)):
        if tracks[i] == "-->":
            v = min(8, v + 2.67)
        elif tracks[i] == "<--":
            v = max(0, v - 2.67)
        elif tracks[i] == "---":
            v = max(0, v - 1)
​
        if i == len(tracks)-1:
            return True
        elif v == 0:
            return i

