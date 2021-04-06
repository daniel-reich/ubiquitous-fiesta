
def most_frequent_char(l):
    l = ''.join(l)
    s = sorted([[i, l.count(i)] for i in set(l)], key=lambda x: x[1], reverse=True)
    return sorted([x[0] for x in s if x[1] == s[0][1]])

