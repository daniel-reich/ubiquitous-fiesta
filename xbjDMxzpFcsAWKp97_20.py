
def can_see_stage(seats):
    s = []
    size = len(seats[0])
    for col in range(size):
        inner = []
        for row in range(len(seats)):
            inner.append(seats[row][col])
        s.append(inner)
    for i in range(len(s)):
        for j in s[i]:
            if s[i].count(j) > 1:
                return False
    for i in range(len(s)):
        if sorted(s[i]) != s[i]:
            return False
    return True

