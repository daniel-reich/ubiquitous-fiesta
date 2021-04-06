
def char_at_pos(r, s):
    lst = [x for i, x in enumerate(r[::-1])
           if i%2 != len(s)%2][::-1]
    if type(r) == str:
        return ''.join(lst)
    return lst

