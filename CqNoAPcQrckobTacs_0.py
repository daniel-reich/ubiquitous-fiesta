
def missing_letter(lst):
    for a, b in zip(lst, lst[1:]):
        if ord(b) - ord(a) > 1:
            return chr(ord(a) + 1)

