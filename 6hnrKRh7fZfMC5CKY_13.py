
def look_and_say(n: int):
    n = str(n)
    l = len(n)
    if l % 2 == 1:
        return 'invalid'
    new_str = ''
    k = 0
    while k < l:
        new_str += n[k+1] * int(n[k])
        k += 2
    return int(new_str)

