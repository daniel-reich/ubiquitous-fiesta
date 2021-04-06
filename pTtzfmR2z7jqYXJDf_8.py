
def possible_palindrome(txt):
    result = sum(filter(lambda x: x%2==1, [txt.count(i) for i in set(txt)]))
    if len(set(txt))==len(txt):
        return False
    else:
        return result == 0 or result%2 == 1

