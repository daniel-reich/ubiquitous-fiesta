
def find_longest(s):
    s = s.replace("'", " ").replace(".", " ").replace('"', "").split()
    return s[0].lower() if len(s) == 1 else find_longest(" ".join(s)) if s.pop(-(len(s[-2]) < len(s[-1]))-1) else None

