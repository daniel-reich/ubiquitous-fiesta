
def possible_palindrome(s):
    return sum([1 for a in [s.count(i) for i in set(s)] if a % 2 == 1]) <= 1

