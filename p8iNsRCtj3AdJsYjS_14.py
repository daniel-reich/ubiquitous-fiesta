
def title_to_number(s):
    r = [ord(i) - 64 for i in s]
    t = [26 ** j[0] * j[1] for j in enumerate(r[::-1])]
    return sum(t)

