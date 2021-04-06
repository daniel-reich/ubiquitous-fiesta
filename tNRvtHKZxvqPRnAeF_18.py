
def digit_occurrences(start, end, digit):
    return ''.join(map(str, list(range(start, end+1)))).count(str(digit))

