
def complete_pattern(s, lst = ""):
    for i in s: lst += i if i not in (lst+"_") else ""
    pos, change, long  = s.find("_"), list(s), len(s)
    for i in lst:
        change[pos] = i; cp = "".join(change)
        for let in range(1, long//2+1):
            for nex in range(let, long+1, let ):
                if cp[nex:nex+let] not in cp[:let]: break
                if nex+let>long: return i

