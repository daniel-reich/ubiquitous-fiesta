
def separate_numbers(s):
    for i in range(len(s) // 2):
        a = int(s[:i + 1])
        t, y = str(a), 1
        while len(str(t)) < len(s):
            t = t + str(a + y)
            y += 1
        if t == s:
            return "YES " + str(a)
    return "NO"

