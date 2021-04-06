
def max_score(s):
    ones = s.count("1")
    start = -(s[0]=="1") + ones + (s[0]=="0")
    mini = start
    for i in s[1:-1]:
        if i == "0":
            start += 1
        else:
            start -= 1
        if start > mini:
            mini = start
    return mini

