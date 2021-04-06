
def is_astonishing(n):
    s = str(n)
    for i in range(1, len(s)):
        a, b = int(s[:i]), int(s[i:])
        total = (a + b)*(abs(a-b) + 1)/2
        if total == n:
            return '{}-Astonishing'.format('AB' if a < b else 'BA')
    return False

