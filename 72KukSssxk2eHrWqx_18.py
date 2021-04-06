
def char_at_pos(r, s):
    x=r[::-1]
    y=x[::2]  if s=="odd" else x[1::2]
    return  y[::-1]

