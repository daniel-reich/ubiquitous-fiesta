
def first_before_second(s, first, second):
    return (len(s) - 1 - s[::-1].find(first)) < s.find(second)

