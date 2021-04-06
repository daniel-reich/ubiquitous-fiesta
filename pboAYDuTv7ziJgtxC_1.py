
def min_turns(current, target):
​
    turns = 0
​
    for ch1, ch2 in zip(current, target):
​
        forward = abs(int(ch2) - int(ch1))
        backward = 10 - forward
​
        turns += min(forward, backward)
​
    return turns

