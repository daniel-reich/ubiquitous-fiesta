
def combinations(start, k, n, count, state, value):
    if k == 0:
        if sum(state) == value:
            count[0] += 1
        return
    for i in range(start, n+1):
        state.append(i)
        combinations(start, k-1, n, count, state, value)
        state.pop()
​
def dice_roll(dice, value):
    count = [0]
    combinations(1, dice, 6, count, [], value)
​
    return count[-1]

