
def generate_word(n):
  if n < 2: return 'invalid'
  out = ['b', 'a']
  def _(n):
    if n < 3:
      return out[-2] + out[-1]
    out.append(out[-2] + out[-1])
    return _(n - 1)
  _(n)
  return ', '.join(out)

