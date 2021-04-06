
def hanoi(n, a=1, b=3):
    c = 6 - a - b
    return hanoi(n-1, a, c) + [(a, b)] + hanoi(n-1, c, b) if n else []

