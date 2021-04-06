
def diamond(carat):
​
    if carat % 2 == 0:
        cut = "good cut"
        diamond = list(list(0 for i in range(carat)) for j in range(carat-1))
        shift = 0.5
    else:
        cut = "perfect cut"
        diamond = list(list(0 for i in range(carat)) for j in range(carat))
        shift = 0
​
    halfCarat = float(carat-1)/2
​
    for i in range(int(halfCarat)+1):
​
        ones = [
            halfCarat - i - shift,
            halfCarat + i + shift
            ]
​
        for j in range(carat):
​
            if j in ones:
                diamond[i][j] = 1
                diamond[-1-i][j] = 1
​
    return [diamond, cut]

