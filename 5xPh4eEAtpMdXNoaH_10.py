
def longest_palindrome(s):
    length = len(s)
    if length <= 1:
        return length
    ans = 2 * sum([s.count(i)//2 for i in set(s) if s.count(i) > 1])
    if ans == length:
        return length
    else:
        return ans + 1

