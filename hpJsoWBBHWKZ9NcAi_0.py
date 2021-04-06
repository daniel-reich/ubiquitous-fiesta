
def bird_code(lst):
  def f(name):
    w=name.replace('-',' ').upper().split()
    s={1:[4],2:[2,2],3:[1,1,2],4:[1,1,1,1]}[len(w)]
    return ''.join(x[:l] for x, l in zip(w, s))
  return list(map(f,lst))

