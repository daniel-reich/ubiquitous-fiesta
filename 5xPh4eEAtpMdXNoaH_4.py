
def longest_palindrome(s):
    p = sum([(1 if i%2 else 0) for i in [s.count(i) for i in set(s)]])
    return len(s) - p + (p != 0)

