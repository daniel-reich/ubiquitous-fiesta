
def digit_occurrences(start, end, n):
    return ''.join(map(str,range(start,end+1))).count(str(n))

