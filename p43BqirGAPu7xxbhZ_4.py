
def diamond(carat):
    middle = (carat) // 2
    rev = middle
    if not carat % 2:
        middle -= 1
    d = [[1 if y == a or y == b else 0 for y in range(carat)] for a, b in enumerate(range(middle, -1, -1), rev)]
    return [d + d[::-1][1:], 'perfect cut'] if carat % 2 else [d + d[::-1][1:], 'good cut']

