
def check_palindrome(ans, num):
    l = num - (abs(num - ans))
    if str(l) == str(l)[::-1]:
        return l
    else:
        return ans
​
def closest_palindrome(num):
    s = str(num)
    if len(s) % 2 == 0:
        mid = (s[0:len(s) // 2])
        ans = int(mid + mid[::-1])
    else:
        mid = (s[0:len(s) // 2 + 1])
        ans = int(mid + mid[::-1][1:])
    return check_palindrome(ans, num)

