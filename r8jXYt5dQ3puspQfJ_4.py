
def split(txt):
  def voweltest(n):
    return 0 if n in 'aeiouAEIOU' else 1
  return ''.join(sorted([i for i in txt], key=voweltest))

