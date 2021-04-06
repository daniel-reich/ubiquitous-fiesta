
def digit_occurrences(start, end, digit):
    nums = range(start, end+1)
    return ''.join(list(map(str, nums))).count(str(digit))

