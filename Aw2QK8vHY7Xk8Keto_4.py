
def longest_word(s):
    s = list(s.split(" "))
    mx = 0
    for i in s:
        if len(i) > mx:
            st = i
            mx = len(i)
    return st

