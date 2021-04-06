
def is_consecutive(s):
    for i in range(1, len(s)):
        if len(s) % i == 0:
            a = [int(s[x : x + i]) for x in range(0, len(s), i)]
            if check(a) or check(a[::-1]):
                return True
    return False
def check(lst):
    return all([lst[i - 1] + 1 == lst[i] for i in range(1, len(lst))])

