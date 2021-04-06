
def is_parsel_tongue(sentence):
    s = sentence.lower().split()
    count = 0
    for i in range(len(s)):
        if s[i].count("s") == 0:
            count += 1
        for x in range(len(s[i]))[:-1]:
            if s[i][x] == "s" and s[i][x + 1] == "s":
                count += 1
                break
    return count == len(s)

