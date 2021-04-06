
def digit_occurrences(start, end, digit):
    occurences = 0
    for number in range(start, end+1):
        occurences += str(number).count(str(digit))
    return occurences

