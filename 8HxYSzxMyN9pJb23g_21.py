
def SplitNCases(s, cases):
    a = len(s)/cases
    if a%1: return ["Error"]
    return [s[i:i+int(a)] for i in range(0, len(s), int(a))]

