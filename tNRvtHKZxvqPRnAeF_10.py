
def digit_occurrences(start, end, digit):
    return sum(str(i).count(str(digit)) for i in range(start, end+1))

