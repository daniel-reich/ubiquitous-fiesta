
def is_palindrome_possible(s):
    can_have_odd = len(s) % 2 == 1
    s = sorted(s)
    counter = 1
    prev = s[0]
​
    for i in range(1, len(s)):
        if prev != s[i]:
            if counter % 2 == 1:
                if can_have_odd:
                    can_have_odd = False
                else:
                    return False
            prev = s[i]
            counter = 1
        else:
            counter += 1
​
    return True

