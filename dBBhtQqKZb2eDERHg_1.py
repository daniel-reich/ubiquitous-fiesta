
def numberSequence(n, seq=""):
    if n <= 0:
        return "-1"
    if seq == "":
        if n == 1:
            return "1"
        if n == 2:
            return "1 1"
        if n % 2 == 0:
            seq = "1 1"
            return numberSequence(n, seq)
        else:
            seq = "1"
            return numberSequence(n, seq)
    l = len(seq.split())
    if l == n:
        return seq.strip()
    last = int(seq.split()[-1])
    seq = str(last + 1) + ' ' + seq + ' ' + str(last + 1)
    return numberSequence(n, seq)

