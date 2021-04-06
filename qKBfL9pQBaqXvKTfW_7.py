
def sum_of_slices(lst):
  p_s, result = 0, []
  for n in lst:
    if p_s + n >= 100:
      result.append(p_s)
      p_s = 0
    p_s += n
  result.append(p_s)
  return result

