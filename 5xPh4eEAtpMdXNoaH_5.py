
def longest_palindrome(s):
    r, one = 0, False
    for i in set(s):
        a = s.count(i)
        if a % 2 == 0:
            r += a
        else:
            r += a - 1
            a = 1
        if a == 1 and one == False:
            r += a
            one = True
    return r

