
def all_about_strings(t):
  m = t[(len(t)//2)-1]+t[len(t)//2] if len(t)%2==0 else t[len(t)//2]
  ind = '@ index {}'.format(t.index(t[1],2)) if t[1] in t[2:] else 'not found'
  return [len(t), t[0], t[-1], m, ind]

