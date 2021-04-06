
def char_at_pos(r, s):
  return (lambda y,x: (x=='odd' and type(y)==str and ''.join(reversed(y))[-2::-2]) or (x=='even' and type(y)==str and ''.join(reversed(y))[::-2]) or (x=='odd' and type(y) == list and len(y)%2 == 0 and [ele for ele in reversed(y)][-2::-2]) or (x=='even' and type(y) == list and len(y)%2 == 0 and [ele for ele in reversed(y)][::-2]) or (x=='odd' and type(y) == list and len(y)%2 == 1 and [ele for ele in reversed(y)][::-2]) or (x=='even' and type(y) == list and len(y)%2 == 1 and [ele for ele in reversed(y)][-2::-2]))(r,s)

