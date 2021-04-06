
def recaman(n):
    if n == 0:
        return ("---> Recaman's sequence: " + str([]) + "\n" + "---> Duplicates for n = " + str(n) + ": " + str([]))
    
    rec, dup = [0], []
    for i in range(1, n):
        if rec[i-1] - i > 0 and rec[i-1] - i not in rec:
            rec.append(rec[i-1] - i)
        else:
            rec.append(rec[i-1] + i)
    for i in range(0, len(rec)):
        if rec[:i+1].count(rec[i]) > 1 and rec[i] not in dup:
            dup.append(rec[i])
​
    return ("---> Recaman's sequence: " + str(rec) + "\n" + "---> Duplicates for n = " + str(n) + ": " + str(dup))

