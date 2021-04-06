
def staircase(n):
  n_abs = abs(n)
​
  def _make_staircase(step):
    if not step:
      return ""
    yield ("#"*step).rjust(n_abs, '_')
    yield from _make_staircase(step-1)
  
  result = [i for i in _make_staircase(n_abs)]
  return '\n'.join(result if n < 0 else result[::-1])

