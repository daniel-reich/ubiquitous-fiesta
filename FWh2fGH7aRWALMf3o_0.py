
def cleave(string, lst):
    words = sorted(lst, key=len, reverse=True)
​
    res = []
    while string:
        found = False
        for i in words:
            if string.endswith(i):
                res.append(i)
                string = string[:-len(i)]
                found = True
                break
        if not found:
            return 'Cleaving stalled: Word not found'
    return ' '.join(res[::-1])

