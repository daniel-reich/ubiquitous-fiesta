
def letter_check(lst):
    first = str(lst[0]).upper()
    second = str(lst[1]).upper()
    for letters in second:
        if letters in first:
            second = second.replace(letters, '', 1)
    if second == '':
        return True
    else:
        return False

