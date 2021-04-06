
def next_number(num):
    s, results = list(str(num))[::-1], []
    for a,b in enumerate(s):
        for c, d in enumerate(s):
            if b > d:
                s[a], s[c] = s[c], s[a]
                temp = sorted([int(e) for e in s[:c]], reverse=True)
                s[:c] = [str(e) for e in temp]
                if int("".join(s[::-1])) > num:
                    results.append(int("".join(s[::-1])))
                s = list(str(num))[::-1]
    results.sort()
    if len(results)> 0: return results[0]
    else: return num

