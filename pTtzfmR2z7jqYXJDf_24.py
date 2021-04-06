
def possible_palindrome(txt):
    t = [txt.count(i) for i in set(txt)]
    if len(set(txt)) == 1:
        return True
    if t.count(1) > 1:
        return False
    return all([False if i % 2 != 0 else True for i in t if i > 1])

