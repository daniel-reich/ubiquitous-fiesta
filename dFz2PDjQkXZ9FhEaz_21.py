
def letter_check(lst):
    return len([i for i in lst[1].lower() if i in lst[0].lower()]) == len(lst[1])

