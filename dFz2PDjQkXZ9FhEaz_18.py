
def letter_check(lst):
    first = set(lst[0].lower())
    second = set(lst[1].lower())
    return (second <= first)

