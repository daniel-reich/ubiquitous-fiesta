
def complete_bracelet(lst):
    seq = "No"
    for i in range(1, len(lst)):
        p1 = lst[0:i+1]
        p2 = lst[i+1:i+3+(i-1)]
        if p1 == p2: 
            lengthtravel = len(p1+p2)
            pattern = p1
            patternlength = len(p1)
            seq = "Yes"
            break
        p1 = []
        p2 = []
    if seq == "No": return False 
    i = lengthtravel
    lst2 = lst[i:].copy()
    while i < len(lst):
        if lst[i:(i+patternlength)] == pattern:
            lst2 = lst2[i+patternlength:]
        i += 1
    if lst2 == []: return True
    return False

