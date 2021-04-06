
def soroban(frame):
    result = [0 for _ in range(7)]
    value = 5
    lower = frame[0]
    upper = frame[4:]
​
    for i, c in enumerate(lower):
        if c == "|":
            result[i] += value
​
    value = 1
    for line in upper:
        for i, c in enumerate(line):
            if c == "|":
                result[i] += value
        value += 1
​
    return sum(10**i * v for i, v in enumerate(result[::-1]))

